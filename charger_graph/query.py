is_charger = 'MATCH (c:Charger {name:$name}) RETURN c'

merge_charger = '''
METGE (charger:Charger { name:$name, meshcode:$meshcode, 
       location:point({$latitude, longitude:$longitude }}))
MATCH (north:Chager { meshcode:$north }),
      (south:Chager { meshcode:$south }),
      (west:Chager { meshcode:$west }),
      (east:Chager { meshcode:$east })
MERGE (charger)-[:LENGTH { length:$ns_length }]->(north)
MERGE (charger)<-[:LENGTH { length:$ns_length }]-(north)
MERGE (charger)-[:LENGTH { length:$ns_length }]->(south)
MERGE (charger)<-[:LENGTH { length:$ns_length }]-(south)
MERGE (charger)-[:LENGTH { length:$we_length }]->(west)
MERGE (charger)<-[:LENGTH { length:$we_length }]-(west)
MERGE (charger)-[:LENGTH { length:$we_length }]->(east)
MERGE (charger)<-[:LENGTH { length:$we_length }]-(east)
'''

update_charger = '''
MATCH (c:$label { name:$name })
SET c.time:$time, c.latest_used=$latest_used, c.latest_stored=$latest_stores, 
    c.after_30min=$after_30min, c.after_60min=$after_60min, c.after_90min=$after_90min, 
    c.after_120min=$after_120min, c.after_150min=$after_150min, c.after_180min=$after_180min
})
'''
