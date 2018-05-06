#I am using Neo4j for an Instagram like app. I chose it because photo sharing 
#apps like that focus on relationships. Photos are displayed on feed primarily 
#by who is followed, which is a relationship
#
#If someone spilled coffee on one of my servers, I would _______
#
#Its not okay to lose the photos, since those are the core content of the app. 
#Photo relationshps are always two way in my implmentation. Also, I will not 
#write a function that overwrites or deletels the property that holds the 
#photos themselves; the photo nodes with comments and tags mus be entirely
# erased.

from py2neo import Graph, Node, Relationship

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
statement = "CREATE (p:Photo {photo:{A}, caption:'A photo', tags:'#dope'})"

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

#transaction to create photo relationships
