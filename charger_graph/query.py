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
SET c.time=$time, c.used_latest=$used_latest, c.stored_latest=$stored_latest

SET c.used_after_30min=$used_after_30min, c.used_after_60min=$used_after_60min 
SET c.used_after_90min=$used_after_90min, c.used_after_120min=$used_after_120min 
SET c.used_after_150min=$used_after_150min, c.used_after_180min=$used_after_180min 

SET c.stored_after_30min=$stored_after_30min, c.stored_after_60min=$stored_after_60min 
SET c.stored_after_90min=$stored_after_90min, c.stored_after_120min=$stored_after_120min 
SET c.stored_after_150min=$stored_after_150min, c.stored_after_180min=$stored_after_180min
'''
