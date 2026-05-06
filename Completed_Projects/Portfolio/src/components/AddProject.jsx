import { useState } from "react";

function AddProject({onAddProject}) {
    const[projectName, setProjectName] = useState('')
    const[description, setDescription] = useState('')

    function handleSubmit(e) {
        e.preventDefault()
    

        const newProject = {
            name: projectName,
            desc: description
        }

        onAddProject(newProject)

        setProjectName('');
        setDescription('');
    }

    return(
        <>
            <form onSubmit = {handleSubmit} className="d-flex flex-column">
                <div className="mb-3">
                    <label htmlFor="projectName" className="form-label fw-bold">Project Name</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="projectName" 
                        value = {projectName}
                        onChange={(e) => setProjectName(e.target.value)}
                        placeholder="Enter the project name"
                        required
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="descriptionTextarea" className="form-label fw-bold">Enter Project description here</label>
                    <textarea 
                        className="form-control" 
                        id="descriptionTextarea" 
                        value = {description}
                        required
                        onChange={(e) => setDescription(e.target.value)}
                        rows="2" 
                        style={{ resize: "none" }}>
                    </textarea>
                </div>

                <button type="submit" className="btn btn-primary w-100 py-2">Add</button>
            </form>
               
        </>
        
    )
}

export default AddProject