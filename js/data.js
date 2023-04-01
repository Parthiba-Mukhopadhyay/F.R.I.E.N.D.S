const { MongoClient } = require('mongodb');

async function main(){

    const uri = "mongodb+srv://pallavguptakumarans:FU3RaEXtckaQCVoD@cluster0.oiyqnkc.mongodb.net/?retryWrites=true&w=majority";

    const client = new MongoClient(uri);

    try{
        await client.connect();
    }
    catch (e) {
        console.error(e)
    }
    finally {
        await client.close();
    }
}

main().catch(console.error);