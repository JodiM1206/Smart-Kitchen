function DeviceCard({ title, status, lastUpdated, readings }) {
  return (
    <div className="device-card">
      <div className="card-top">
        <h2>{title}</h2>
        <span className={`status ${status}`}>{status}</span>
      </div>

      <div className="readings">
        {readings.map((r) => (
          <div className="reading" key={r.label}>
            <div className="reading-value">
              {r.value}
              <span className="reading-unit">{r.unit}</span>
            </div>
            <div className="reading-label">{r.label}</div>
          </div>
        ))}
      </div>

      <p className="last-updated">Last updated {lastUpdated}</p>
    </div>
  )
}

export default DeviceCard