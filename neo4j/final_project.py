#I am using Neo4j for an Instagram like app. I chose it because photo sharing 
#apps like that focus on relationships. Photos are displayed on feed primarily 
#by who is followed, which is a relationship
#
#If someone spilled coffee on one of my servers, I would cry, 
#beacause aside from some data in the graph computation engine, almost all my data would be lost.
#
#Its not okay to lose the photos, since those are the core content of the app. 
#Photo relationshps are always two way in my implmentation. 
#Also, I use a transaction when a user uploads a photo, 
#to ensure that all the two relationships that come with the photo exist with the photo. 

from py2neo import Graph

graph = Graph()

#transaction to create the three user nodes
tx = graph.cypher.begin()
statement = "CREATE (u:User {name: {A}})"

for user_a in ["Kawhi", "Joel", "Lebron"]:
    tx.append(statement, {"A": user_a})

tx.commit

#transaction to create 15 photos. 
#Note that I'm using strings instead of actual photos
tx = graph.cypher.begin()
statement = "CREATE (p:Photo {title:{A}, photo:'p', likes:0, time:timestamp(), caption:'A photo'})"

photo_placeholder = ['basket','ball','banana','boat','tennis','shoe','ham','string','funny','bone','t','shirt','hard','wood','dog']

for photo_a in photo_placeholder:
    tx.append(statement, {'A': photo_a})

tx.commit


#transaction to create the relationships between users
tx = graph.cypher.begin()
statement = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:FOLLOWS]->(b)"

user_rels = [("Lebron", "Joel"), ("Lebron","Kawhi"), ("Joel", "Lebron"), ("Joel", "Kawhi"), ("Kawhi", "Joel")]:

for user_a, user_b in user_rels:
    tx.append(statement, {'A': user_a, 'B': user_b})

tx.commit

#transaction to create User to photo relationships
tx = graph.cypher.begin()
statement = "MATCH (a:User {name:{A}}), (b:Photo {title:{B}}) CREATE (a)-[:HAS]->(b)"

user_to_photo = [("Lebron", "basket"), ("Lebron","ball"), ('Lebron','bannan'),('Lebron','boat'),('Lebron','tennis'),("Joel", "shoe"), ("Joel", "ham"), ('Joel','string'), ('Joel','funny'), ('Joel','bone'),("Kawhi", "t"),('Kawhi','shirt'),('Kawhi','hard'),('Kawhi','wood'),('Kawhi','dog')]:

for user, photo in user_to_photo:
    tx.append(statement, {'A': user, 'B': photo})

tx.commit

#tansaction to create photo to User relationships
tx = graph.cypher.begin()
statement = "MATCH (a:Photo {title:{A}}), (b:User {name:{B}}) CREATE (a)-[:IS_HAD]->(b)"

photo_to_user = [("basket","Lebron"), ("ball","Lebron"), ('banana','Lebron'),('boat','Lebron'),('tennis','Lebron'),("shoe","Joel"), ("ham","Joel"), ('string','Joel'), ('funny','Joel'), ('bone','Joel'),("t","Kawhi"),('shirt','Kawhi'),('hard','Kawhi'),('wood','Kawhi'),('dog','Kawhi')]:

for photo, user in photo_to_user:
    tx.append(statement, {'A': photo, 'B': user})

tx.commit

#action 1: A new user signs up for an account

graph.cyber.execute("CREATE (u:User {name:{T}}",{'T':'Tim'})

#action 2: Tim follows Kawhi and Lebron

tx = graph.cypher.begin()
statement = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:FOLLOWS]->(b)"

user_rels = [("Tim", "Lebron"), ("Tim", "Kawhi")]:

for user_a, user_b in user_rels:
    tx.append(statement, {'A': user_a, 'B': user_b})

tx.commit

#action 3: Tim views Kawhi's photos

statement = "MATCH (u:User {name:'Tim'})-->(v:User {name:'Kawhi'})-->(p:Photo) RETURN p.title AS title"

for record in graph.cypher.execute(statement):
    print(record.title)

#action 4: Tim likes one of Kawhi's photos
statement = "MATCH (u:User {name:'Tim'})-->(v:User {name:'Kawhi'})-->(p:Photo {title:'dog'}) SET p.likes += 1"

graph.cypher.execute(statement)

#action 5: Tim comments on one of Kawhi's photos
statement = "MATCH (u:User {name:'Tim'})-->(v:User {name:'Kawhi'})-->(p:Photo {title:'dog'}) SET p.comment = 'I like your dog.'"

graph.cypher.execute(statement)

#action 6: Tim gets a follow back!
statement = "MATCH (a:User {name:Kawhi}), (b:User {name:Tim}) CREATE (a)-[:FOLLOWS]->(b)"

graph.cypher.execute(statment)

#action 7: Tim posts a photo

tx = graph.cypher.begin()

statement0 = "CREATE (p:Photo {title:'kite_karate, photo:'p', likes:0, time:timestamp(), caption:'The sickest thing you will ever see'})"
statement1 = "MATCH (p:Photo {title:'kite_karate'}), (u:User {name:'Tim'}) CREATE (p)-[:IS_HAD]->(u)"
statement2 = "MATCH (u:User {name:'Tim'}), (p:Photo {title:'kite_karate'}) CREATE (u)-[:HAS]->(p)"

for s in [statement0, statement1, statement2]:
    tx.append(s)

tx.commit()

#action 8: Tim Likes his own photo

statement = "MATCH (u:User {name:'Tim'})-[:HAS]->(p) SET p.likes += 1"

graph.cypher.execute(statement)





