$( document ).ready(function () {
  // Create service card
  function createServiceCard(service) {
    return `
      <a href="#">
        <div class="card">
          <img src="{{ url_for('static', filename='images/tailor.jpeg') }}" class="card-img-top" alt="${ service.name }">
          <div class="card-footer">
            <p class="text-body-secondary text-bold">${ service.name }</p>
          </div>
        </div>
      </a>
    `;
  }
  // Extract data from the embedded JSON
  const services = JSON.parse($('#services').html());

  
  // Dynamically update the available artisans
  const availableServices = () => {
    services.forEach((service) => {
      $('#service-card').append(createServiceCard(service));
    });
  }

  availableServices();
    
});