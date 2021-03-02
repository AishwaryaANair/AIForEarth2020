mapboxgl.accessToken = 'pk.eyJ1IjoiamF5ZGJlbmRyZSIsImEiOiJja2xyaWhvOWQxbXQyMm5xeTFiczlzZjllIn0.fQyC6d6ezU7eA3daw4Lp8g';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
    center: [31.4606, 20.7927],
    zoom: 0.5
});


function filterBy(start_date, end_date) {
    console.log(start_date, end_date)
    // date_array = range(start_date, end_date)
    var filters = ["all", ["<=", "date", end_date], [">=", "date", start_date]];
    map.setFilter('forestfires-circles', filters);
    map.setFilter('forestfires-labels', filters);

    // Set the label to the month

}

map.on('load', function () {

    d3.json(
        '../static/json/created_data_abridged.json',
        function (err, data) {
            if (err) throw err;

            // Create a month property value based on time
            // used to filter against.
            data.features = data.features.map(function (d) {
                d.properties.day = new Date(d.properties.date).getDate();
                d.constant = 1
                return d;
            });
            console.log(data)
            map.addSource('forestfires', {
                'type': 'geojson',
                data: data
            });

            map.addLayer({
                'id': 'forestfires-circles',
                'type': 'circle',
                'source': 'forestfires',
                'paint': {
                    'circle-color': [
                        'interpolate',
                        ['linear'],
                        ['get', 'constant'],
                        6,
                        '#FCA107',
                        8,
                        '#7F3121'
                    ],
                    'circle-opacity': 0.75,
                    'circle-radius': [
                        'interpolate',
                        ['linear'],
                        ['get', 'constant'],
                        6,
                        20,
                        8,
                        40
                    ]
                }
            });

            map.addLayer({
                'id': 'forestfires-labels',
                'type': 'symbol',
                'source': 'forestfires',
                'layout': {
                    'text-field': [
                        'concat',
                        ['to-string', ['get', 'constant']],
                        'm'
                    ],
                    'text-font': [
                        'Open Sans Bold',
                        'Arial Unicode MS Bold'
                    ],
                    'text-size': 12
                },
                'paint': {
                    'text-color': 'rgba(0,0,0,0.5)'
                }
            });


            filterBy(new Date(2021, 02, 01).getTime(), new Date(2021, 02, 02).getTime());
        }
    );
});

