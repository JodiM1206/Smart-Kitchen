import { devices } from './mockData'
import DeviceCard from './DeviceCard'

function Dashboard() {
  return (
    <main className="dashboard">
      {devices.map((device) => (
        <DeviceCard key={device.id} {...device} />
      ))}
    </main>
  )
}

export default Dashboard