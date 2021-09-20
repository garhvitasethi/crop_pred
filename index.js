const express = require('express')
const { spawn } = require('child_process')
const app = express()
const path=require("path");
const bodyParser = require('body-parser');

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.resolve(__dirname,'public')));

app.post('/submit', (req, res) => {

  const get_key = (val,dict) => {
    for (const [key, value] of Object.entries(dict)) {
      if(value==val)
        return key
    }
  }
  const { district, year, season, area, rain, temperature } = req.body
    const python = spawn('python', ["model2.py",district, year, season, area, rain, temperature])

    var output=""
    python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...')
      // console.log(data.toString())
      output+=data
    })
    python.stdout.on('close', function (code) {
        console.log('Closed with code ',code)
        console.log("Output is ",output.trim().split('\r\n'))
        output = output.split("finalprint")[1]
        const districts = ['AMRITSAR', 'BATHINDA', 'FARIDKOT', 'FATEHGARH SAHIB', 'FIROZPUR', 'GURDASPUR', 'HOSHIARPUR', 'JALANDHAR', 'KAPURTHALA', 'LUDHIANA', 'MANSA', 'MOGA', 'MUKATSAR', 'NAWANSHAHR', 'PATIALA', 'ROPAR(RUPNAGAR)', 'SANGRUR']
        const seasons = ['Kharif','Rabi','Whole year']
        res.render('pages/image',{data: output ? output.trim().split('\r\n') : ["Sugarcane","Sunflower","Urad"],input:{district:districts[district], year, season:seasons[season], area, rain, temperature}});
      })

    
})

app.get('/check',(req,res)=>{
  console.log("Check Route")
  res.render('pages/image',{data: "Mosaic.jpeg"});
})

app.get('/',(req,res)=>{
  console.log("Home Route")
  res.render('pages/index');
})

const PORT = process.env.PORT || 5000;


app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}!`)
})
