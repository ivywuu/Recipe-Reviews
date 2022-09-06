import React, {useState,useEffect} from 'react'
import ListItem from '../components/ListItem'

const Tools = () => {

  let [tools, setTools] = useState([])

  useEffect(() => {
    getTools()
  }, [])

  let getTools = async () => {
    let response = await fetch('/api/tools/')
    let data = await response.json()
    console.log('DATA:',data)
    setTools(data)
  }


  return (
    <div>
      <div className="recipe-list">
        {tools.map((tool, index) => (
          <ListItem key={index} tool={tool}/>
        ))}
      </div>
    </div>
  )
}

export default Tools