import { useState } from 'react'
import './App.css'
import AddProject from './components/AddProject'
import SearchProject from './components/SearchProject'
import ProjectList from './components/ProjectList'

function App() {
  const[projects, setProjects] = useState([])
  const[searchProject, setSearchProject] = useState('')

  const handleAddProject = (newProject) => {
    setProjects((prevProjects) => [...prevProjects, newProject])
  }

  const filteredProjects = projects.filter((project) => 
    project.name.toLowerCase().includes(searchProject.toLowerCase()))
  
  return(
    <div>
      <div>
        <h1>Personal Project Showcase App</h1>
        <AddProject onAddProject={handleAddProject}/>
        <SearchProject searchProject={searchProject} setSearchProject={setSearchProject}/>
        <ProjectList projectsList={filteredProjects} />

      </div>
    </div>
  )
}

export default App