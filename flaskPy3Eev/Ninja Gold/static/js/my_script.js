// Add an event listener for all video containers 
// in order to play the video when the mouse enter and pause it when the mouse leave  

const videoBackgrounds = document.querySelectorAll('.video-background'); // Get all video containers

videoBackgrounds.forEach(function(videoBackground) { 
    const video = videoBackground.querySelector('.video');      // Get the video inside it 
    
    videoBackground.addEventListener('mouseenter', function() { // Add an event listener when mouse enter 
        video.play();                                           // Play the video 
    });

    videoBackground.addEventListener('mouseleave', function() { // Add an event listener when mouse leasve 
        video.pause();                                          // Pause the video 
    });
});