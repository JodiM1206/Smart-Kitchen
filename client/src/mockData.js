export const devices = [
    {
        id: 'fridge',
        title: 'Fridge',
        status: 'online',
        lastUpdated: '2 min ago',
        readings: [
            { label: 'Temperature', value: 3.8, unit: '°C' },
            { label: 'Humidity', value: 41, unit: '%' },
        ],
    },
    {
        id: 'pantry',
        title: 'Pantry Scale',
        status: 'online',
        lastupdated: '5 min ago',
        readings: [{label: 'Weight', value: 1250, unit: 'g'}],
    },
    {
        id: 'leak',
        title: 'Leak Detector',
        status: 'offline',
        lastUpdated: '3 hours ago',
        readings: [{label: 'Status', value: 'Dry', unit: ''}],
    },
]