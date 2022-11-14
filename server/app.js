// from https://expressjs.com/en/starter/hello-world.html

const express = require('express')
const app = express()
const port = 8000
const cors = require('cors')

app.use(express.json());
app.use(cors())

itemStore = {}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/html');
  res.send(Buffer.from(" <html> <head> <title>I'm Sorry I think You're Lost....</title></head><body><h1>I'm Sorry I think You're Lost....</h1> <h2>This is not the page you are looking for</h2> </body></html>"));
})

app.post('/item/', (req, res) => {
    if (!req.user_id && !req.body.description && !req.body.keywords && !req.body.lat && !req.body.lon) {
      return res.status(405).json({message: 'missing fields'})
    }
    d = new Date();
    max_val = Math.max( ...Object.keys(itemStore)) + 1;
    if (max_val == -Infinity){
      max_val = 1
    }
    itemId = {"id": max_val}
    itemDate = {"date_from": d.toISOString().slice(0, 10),"date_to": d.toISOString().slice(0, 10)}
    itemStore[max_val] = Object.assign(itemId, req.body, itemDate);

    res.status(201).json(itemStore[max_val])

})


app.get('/items/', (req, res) => {
  if(req.query.user_id)
  {
    res.status(200).json(Object.values(itemStore).filter(i  => i.user_id == req.query.user_id))
    return;
  }
  if(req.query.date_from)
  {
    res.status(200).json(Object.values(itemStore).filter(i  => i.date_from == req.query.date_from))
    return;
  }
  res.status(200).json(Object.values(itemStore))
})

app.get('/item/:id', (req, res) => {
  const id = parseInt(req.params.id)
  if(Object.keys(itemStore).includes(req.params.id)){
      res.status(200).json(itemStore[id])
  }
  else{
      res.status(404).send('Item not found')
  }
})

app.delete('/item/:id', (req, res) => {
  const id = parseInt(req.params.id)
  if(Object.keys(itemStore).includes(req.params.id)){
      delete itemStore[id]
      res.status(204).json(itemStore[id])
  }
  else{
      res.status(404).send('Item not found')
  }
})


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

// https://expressjs.com/en/guide/error-handling.html
app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).send('Something broke!')
})

// Docker container exit handler
// https://github.com/nodejs/node/issues/4182
process.on('SIGINT', function() {
    process.exit();
})