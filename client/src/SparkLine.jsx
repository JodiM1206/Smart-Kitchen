function SparkLine({ data, threshold, width = 240, height = 60}){
    const values = threshold === undefined ? data : [...data, threshold]
    const min = Math.min(...data)
    const max = Math.max(...data)
    const range = max - min || 1
    const pad = 4

    const toY = (value) => 
        pad + (1 - ( value - min) / range) * (height - pad * 2)

    const points = data
      .map((value, i) => `${(i / (data.length - 1)) * width},${toY(value)}`)
      .join(' ')

      return (
        <svg 
        className="sparkline"
        viewBox={`0 0 ${width} ${height}`}
        preserveAspectRatio="none"
        >
          {threshold !== undefined && (
            <line 
              x1="0"
              x2={width}
              y1={toY(threshold)}
              y2={toY(threshold)}
              stroke="#16a34a"
              strokeWidth="1.5"
              strokeDasharray="6 4"
              vectorEffect="non-scaling-stroke"
            />  
          )}  
          <polyline
            points={points}
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            vectorEffect="non-scaling-stroke"
            />
        </svg>
      )
}

export default SparkLine