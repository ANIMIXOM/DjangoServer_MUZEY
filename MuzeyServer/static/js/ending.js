window.addEventListener('message', function(event) {
            if (event.data === 'windowClosed') {
                console.log('Окно в iframe закрыто');
                window.location.replace('/add_score/');
            }
        });