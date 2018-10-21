var map;
var fromto = [];
var path = [];
var linkmap = {}, nodemap = {};

$(function() {
	const marker_norm = {radius: 6, fillOpacity: 0.85, color: '#4444ff', fillColor: '#0000ff', weight: 1, pane: 'markerPane'};
	const marker_sel = {radius: 8, fillOpacity: 1.0, color: '#ff4444', fillColor: '#ff0000', weight: 1, pane: 'markerPane'};
	const link_norm = {weight: 3, opacity: 0.85, color: '#8888ff'};
	const link_sel = {weight: 6, opacity: 1.0, color: '#ff0000'};
	const popup_names = ['from', 'to'];

	function clearPath() {
		for (var i = 0; i < fromto.length; i++) {
			fromto[i].setStyle(marker_norm);
			fromto[i].closePopup();
			fromto[i].unbindPopup();
		}
		fromto.length = 0;
		for (var i = 0; i < path.length; i++) {
			path[i].setStyle(link_norm);
		}
		path.length = 0;
	}

	$.getJSON('/api/config', function(json) {
		console.log(json);
		map = L.map('map').setView(json.center, 17);
		map.on('contextmenu', function(event) {
			clearPath();
		});

		var tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>'
		});
		tileLayer.addTo(map);

		$.getJSON('/data/node.geojson', function(json) {
			nodes = json;
			var layer = L.geoJson(nodes, {
				style: marker_norm,
				pointToLayer: function(feature, latlng) {
					var marker = new L.CircleMarker(latlng, marker_norm);
					marker.on('click', function(event) {
						var marker = event.target;
						if ( fromto.length >= 2 ) {
							clearPath();
						}
						marker.setStyle(marker_sel);
						marker.bindPopup(popup_names[fromto.length], {
							closeButton: true,
							closeOnClick: false,
							autoClose: false,
						}).openPopup();
						fromto.push(marker);
						if ( fromto.length >= 2 ) {
							$.ajax({
								type: 'post',
								url: '/api/dijkstra',
								data: JSON.stringify({
									start: (fromto[0].feature.properties['ノードID'] || fromto[0].feature.properties['id']),
									end: (fromto[1].feature.properties['ノードID'] || fromto[1].feature.properties['id'])
								}),
								contentType: 'application/json',
								dataType: 'json',
								success: function(json) {
									path = json.map(function(e) { return linkmap[e] });
									for (var i = 0; i < path.length; i++) {
										path[i].setStyle(link_sel);
									}
								},
								error: function(json) {
									alert('エラーが発生しました。Pythonのコードを見直してください。' + json);
									console.log("error", json);
								}
							});
						}
					});
					return marker;
				},
				onEachFeature: function(feature, layer) {
					var id = (feature.properties['ノードID'] || feature.properties['id']);
					if ( !id ) return;
					nodemap[id] = layer;
				},
			});
			layer.addTo(map);
		});

		$.getJSON('/data/link.geojson', function(json) {
			links = json;
			var layer = L.geoJson(links, {
				style: link_norm,
				onEachFeature: function(feature, layer) {
					var id = (feature.properties['リンクID'] || feature.properties['id']);
					if ( !id ) return;
					linkmap[id] = layer;
				},
			});
			layer.addTo(map);
		});
	});
});
