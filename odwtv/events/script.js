$(document).ready(function () {
    // Fetch the JSON data from the text file
    $.ajax({
        url: 'events.json', // Make sure the path is correct
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // Process the JSON data and display it as a list
            displayEventList(data);
        },
        error: function (error) {
            console.error('Error loading JSON:', error);
        }
    });

    function displayEventList(events) {
        var $eventContainer = $('#eventContainer');
        events.forEach(function (event) {
            var eventHtml = '<div class="event" style="background-image: url(\'' + event.image + '\');">' +
                '<div class="event-details">' +
                '<strong></strong> ' + event.name + '<br>' +
                '<strong></strong> ' + event.date + '<br>' +
                '<strong></strong> ' + calculateTimeUntil(event.date) +
                '</div>' +
                '<div class="event-description">' + event.description + '</div>' +
                '</div>';

            $eventContainer.append(eventHtml);
        });
    }

    function calculateTimeUntil(eventDate) {
        var now = new Date();
        var eventDateTime = new Date(eventDate);
        var timeUntil = eventDateTime - now;

        var days = Math.floor(timeUntil / (1000 * 60 * 60 * 24));
        var hours = Math.floor((timeUntil % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((timeUntil % (1000 * 60 * 60)) / (1000 * 60));

        return days + 'd ' + hours + 'h ' + minutes + 'm';
    }
});
