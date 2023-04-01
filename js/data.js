const { MongoClient } = require('mongodb');

async function main(){

    const uri = "mongodb+srv://pallavguptakumarans:FU3RaEXtckaQCVoD@cluster0.oiyqnkc.mongodb.net/?retryWrites=true&w=majority";

    const client = new MongoClient(uri);

    try{
        await client.connect();
        await listDatabases(client)
    }
    catch (e) {
        console.error(e)
    }
    finally {
        await client.close();
    }
}

main().catch(console.error);

async function listDatabases(client){
    const dblis = await client.db().admin().listDatabases();
    console.log("Databases");
    dblis.databases.forEach(db => {
        console.log(' -${db.name}');
    });
}