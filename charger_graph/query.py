is_charger = 'MATCH (c:Charger {name:$name}) RETURN c'

merge_charger = '''
MATCH (north:Mesh { meshcode:$north }),
      (south:Mesh { meshcode:$south }),
      (west:Mesh { meshcode:$west }),
      (east:Mesh { meshcode:$east }) 
MERGE (charger:Charger { name:$name, meshcode:$meshcode, 
       latitude:$latitude, longitude:$longitude}) 
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
MATCH (c:Charger { meshcode: $meshcode }) 
SET c.time=$time, c.latest_used=$latest_used, c.latest_stored=$latest_stored
SET c.after_30min=$after_30min, c.after_60min=$after_60min, c.after_90min=$after_90min 
SET c.after_120min=$after_120min, c.after_150min=$after_150min, c.after_180min=$after_180min
'''
