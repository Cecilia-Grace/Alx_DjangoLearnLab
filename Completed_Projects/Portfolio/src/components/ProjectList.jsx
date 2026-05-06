function ProjectList({ projectsList }) {
    return (
      <div className="mt-4">
        <h3>Project List ({projectsList.length})</h3>
        {projectsList.length > 0 ? (
          <div className="row">
            {projectsList.map((p, index) => (
              <div key={index} className="col-md-6 mb-3">
                <div className="card h-100 border-0 shadow-sm">
                  <div className="card-body">
                    <h5 className="card-title text-primary">{p.name}</h5>
                    <p className="card-text text-muted">{p.desc}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <p className="text-muted text-center py-4">No projects found.</p>
        )}
      </div>
    )
}
  
export default ProjectList
  