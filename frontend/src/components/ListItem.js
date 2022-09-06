import React from 'react'

const ListItem = ({ tool }) => {
  return (
    <div>
      <img src={tool.pic} alt="" />
    </div>
  )
}

export default ListItem