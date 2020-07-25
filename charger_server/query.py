is_charger = 'MATCH (c:Charger {name:$name, time:$time}) RETURN c'

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

# update_charger = '''
# MATCH (c:Charger { meshcode: $meshcode })
# SET c.time=$time, c.used_latest=$used_latest, c.stored_latest=$stored_latest
#
# SET c.used_after_30min=$used_after_30min, c.used_after_60min=$used_after_60min
# SET c.used_after_90min=$used_after_90min, c.used_after_120min=$used_after_120min
# SET c.used_after_150min=$used_after_150min, c.used_after_180min=$used_after_180min
#
# SET c.stored_after_30min=$stored_after_30min, c.stored_after_60min=$stored_after_60min
# SET c.stored_after_90min=$stored_after_90min, c.stored_after_120min=$stored_after_120min
# SET c.stored_after_150min=$stored_after_150min, c.stored_after_180min=$stored_after_180min
# '''

update_charger = ''' 
MATCH (north:Mesh { meshcode:$north }),
      (south:Mesh { meshcode:$south }),
      (west:Mesh { meshcode:$west }),
      (east:Mesh { meshcode:$east }) 

CREATE (charger:$Label { name:$name, meshcode:$meshcode, 
                           latitude:$latitude, longitude:$longitude,
                           time:$time, used_latest:$used_latest, stored_latest:$stored_latest,
                           used_after_030:$used_after_030, used_after_060:$used_after_060,
                           used_after_090:$used_after_090, used_after_120:$used_after_120,
                           used_after_150:$used_after_150, used_after_180:$used_after_180,
                           stored_after_030:$stored_after_030, stored_after_060:$stored_after_060,
                           stored_after_090:$stored_after_090, stored_after_120:$stored_after_120,
                           stored_after_150:$stored_after_150, stored_after_180:$stored_after_180 }) 

CREATE (charger)-[:LENGTH { length:$ns_length }]->(north) 
CREATE (charger)<-[:LENGTH { length:$ns_length }]-(north) 
CREATE (charger)-[:LENGTH { length:$ns_length }]->(south) 
CREATE (charger)<-[:LENGTH { length:$ns_length }]-(south) 
CREATE (charger)-[:LENGTH { length:$we_length }]->(west) 
CREATE (charger)<-[:LENGTH { length:$we_length }]-(west) 
CREATE (charger)-[:LENGTH { length:$we_length }]->(east) 
CREATE (charger)<-[:LENGTH { length:$we_length }]-(east)
'''
