

  
      function setGradientBasedOnTime() {
        const now = new Date();
        const hours = now.getHours(); 
      
        let color1, color2;
      
        if (hours >= 6 && hours < 12) {
            // Morning
            color1 = '#87CEEB';  // Sky Blue
            color2 = '#FFD700';  // Gold 
        } else if (hours >= 12 && hours < 18) {
            // Afternoon
            color1 = '#FFA07A';  // Light Salmon
            color2 = '#FF6347';  // Tomato 
        } else {
            // Evening/Night
            color1 = '#483D8B';  // Dark Slate Blue
            color2 = '#8A2BE2';  // Blue Violet 
        }
      
        const gradient = `linear-gradient(to right, ${color1}, ${color2})`;
      
        document.body.style.background = gradient;
        document.getElementById('time').style.background = gradient;
      }
      
      // Set the initial gradient
      setGradientBasedOnTime();
      
      // Update the gradient every minute (you can adjust the interval as needed)
      setInterval(setGradientBasedOnTime, 60000);