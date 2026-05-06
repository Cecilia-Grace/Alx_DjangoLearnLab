import { useState } from "react"

function SearchProject({searchProject, setSearchProject}) {
    return(
        <div className="my-4">
            <input
                type="text"
                className="form-control form-control-lg shadow-sm"
                placeholder="Search projects..."
                value={searchProject}
                onChange={(e) => setSearchProject(e.target.value)} 
            />
    </div>
    )
}

export default SearchProject