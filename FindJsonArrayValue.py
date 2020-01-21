db={
    "Streams":{
"Stream1":{
    "Stream1Table1":["s1Table1Column1","s1Table1Column2","s1Table1Column3"],
    "Stream1Table2":["s1Table2Column1","s1Table2Column2","s1Table2Column3"],
    },
"Stream2":{
"Stream2Table1":["s2Table1Column1","s2Table1Column2","s2Table1Column3"],
"Stream2Table2":["s2Table2Column1","s2Table2Column2","s2Table2Column3"]
    }
}
    }

persist = "Infinite Entry"
print("\n\t\t\t Json Array values Finder in Python(3.8.1)\n")
while persist != "Exit":
    ref=input("\t\tEnter the Value:")
    print("\n\t\tSearch Results:\n")
    for stream in db['Streams']:
        for table in db['Streams'][stream]:
            TotalColumns = len(db['Streams'][stream][table])
            for column in range(0,TotalColumns):
                    if ref.lower() == (db['Streams'][stream][table][column].lower()):
                         print("\t\tStream:"+stream+"\n"+"\t\tTable:"+table+"\n"+"\t\tColumn:"+db['Streams'][stream][table][column]+"\n")
