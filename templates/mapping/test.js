request.onreadystatechange = function() {
	    if (request.readyState == 4) {
		var xmlsource = request.responseXML;
		var markerlist = xmlsource.documentElement.getElementsByTagName("city");
		for (var i=0;i < markerlist.length;i++) {
		    addmarker(parseFloat(markerlist[i].getAttribute("lng")),
			      parseFloat(markerlist[i].getAttribute("lat")),
			      markerlist[i].getAttribute("title"));
		    popdata[i] = new Array();
		    var poplist = markerlist[i].getElementsByTagName("pop");
		    for (var j=0;j<poplist.length;j++) {
			popdata[i][poplist[j].getAttribute("year")] = parseInt(poplist[j].getAttribute("value"));
			years[poplist[j].getAttribute("year")] = 0;
		    }
		}
		for (var i in years) {
		    yearpanel.innerHTML = yearpanel.innerHTML + 
			'<a href="#" onClick="addgraph(' + i + ')">' + i + '</a><br/';
		}
		recenterandzoom(points);
	    }
	}
	
