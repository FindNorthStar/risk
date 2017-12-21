$(function () {

    var employeeData;

    $.ajax({method: 'get', url: '/employseason.json'}).done(function (data) {

        employeeData = data.employ_data;
        // console.log(employeeData);

        Morris.Area({
            element: 'morris-area-chart',
            data: employeeData,
            xkey: 'period',
            // ykeys: ['employee'],
            ykeys: ['employee','bachlor','no_degree'],
            // labels: ['employee'],
            labels: ['employee','bachlor','no_degree'],
            pointSize: 2,
            hideHover: 'auto',
            resize: true
        });

    }).fail();

    $.ajax({method: 'get', url: '/employlevel.json'}).done(function (data) {

        employeeData = data.education_data;
        // console.log(employeeData);

        Morris.Donut({
            element: 'morris-donut-chart',
            data: employeeData,
            resize: true
        });

    }).fail();


    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });


});
