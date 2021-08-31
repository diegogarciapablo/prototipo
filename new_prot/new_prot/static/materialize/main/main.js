//boton de accion flotante

//barra de navegacion
const elemsDropdown = document.querySelectorAll(".dropdown-trigger");
const instancesDropdown = M.Dropdown.init(elemsDropdown,{
	coverTrigger: false,
	constrainWidth: false
	});

const elemsSidenav = document.querySelectorAll(".sidenav");
const instancesSidenav = M.Sidenav.init(elemsSidenav,{
	edge: "left"
});

const elemsModal = document.querySelectorAll('.modal');
const instancesModal = M.Modal.init(elemsModal);

const elemsCarrusel = document.querySelectorAll('.carousel');
const instancesCarrusel = M.Carousel.init(elemsCarrusel,{
	duration : 200,
	indicators: true,

	});
