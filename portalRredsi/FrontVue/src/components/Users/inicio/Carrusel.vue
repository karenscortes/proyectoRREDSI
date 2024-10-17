<template>
    
    <div class="home">

        <!-- Hero Slider -->
        <div class="hero_slider_container">
            <div class="hero_slider owl-carousel">

                <!-- Hero Slide -->
                <div class="hero_slide">
                    <div class="hero_slide_background"></div>
                    <div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
                        <div class="hero_slide_content text-center">
                            <h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Inscripciones
                                <span>abiertas</span> 2024!
                            </h1>
                        </div>
                    </div>
                </div>

                <!-- Hero Slide -->
                <div class="hero_slide">
                    <div class="hero_slide_background"></div>
                    <div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
                        <div class="hero_slide_content text-center">
                            <h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Evaluadores
                                <span>certificados</span> !
                            </h1>
                        </div>
                    </div>
                </div>

                <!-- Hero Slide -->
                <div class="hero_slide">
                    <div class="hero_slide_background"></div>
                    <div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
                        <div class="hero_slide_content text-center">
                            <h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Proyectos
                                <span>investigativos</span> !
                            </h1>
                        </div>
                    </div>
                </div>

            </div>

            <div class="hero_slider_left hero_slider_nav trans_200"><span class="trans_200">Ant</span></div>
            <div class="hero_slider_right hero_slider_nav trans_200"><span class="trans_200">Sig</span></div>
        </div>
    </div>
    <div class="hero_boxes">
        <div class="hero_boxes_inner">
            <div class="container">
                <div class="row">

                    <div class="col-lg-4 hero_box_col">
                        <div class="hero_box d-flex flex-row align-items-center justify-content-start">
                            <img src="../../../assets/img/books.svg" class="svg" alt="">
                            <div class="hero_box_content">
                                <h2 class="hero_box_title">Convocatorias</h2>
                                <a href="https://rredsi.com.co/xiv-encuentro-departamental-de-semilleros-de-investigacion-de-risaralda/"
                                    class="hero_box_link">ver más</a>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-4 hero_box_col">
                        <div class="hero_box d-flex flex-row align-items-center justify-content-start">
                            <img src="../../../assets/img/earth-globe.svg" class="svg" alt="">
                            <div class="hero_box_content">
                                <h2 class="hero_box_title">RREDSI</h2>
                                <a href="https://rredsi.com.co/" class="hero_box_link">ver más</a>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-4 hero_box_col">
                        <div class="hero_box d-flex flex-row align-items-center justify-content-start">
                            <img src="../../../assets/img/professor.svg" class="svg" alt="">
                            <div class="hero_box_content">
                                <h2 class="hero_box_title">Pertenecer</h2>
                                <a href="https://www.youtube.com/watch?v=mZcP6q_i3EI" target="_blank" class="hero_box_link">ver
                                    más</a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>
import '../../../assets/plugins/OwlCarousel2-2.2.1/owl.carousel.css';
import '../../../assets/plugins/OwlCarousel2-2.2.1/owl.theme.default.css';
import '../../../assets/plugins/OwlCarousel2-2.2.1/animate.css';
import '../../../assets/plugins/OwlCarousel2-2.2.1/owl.carousel.js';
export default {
	mounted() {
		this.initializeCarousel(); // Inicializa el carrusel cuando el componente se monta
	},
	beforeUnmount() {
		
		this.destroyCarousel(); // Destruye el carrusel antes de que el componente se destruya
	},
	methods: {
		initializeCarousel() {

			const $carousel = $('.owl-carousel');
			
			// Destruir cualquier instancia existente de Owl Carousel
			if ($carousel.hasClass('owl-loaded')) {
			$carousel.trigger('destroy.owl.carousel');
			$carousel.removeClass('owl-loaded'); // Eliminar clase de estado
			}
			
			// Inicializar el nuevo carrusel
			$carousel.owlCarousel({
			loop: true,
			margin: 10,
			nav: false,
			items: 1,
			autoplay: true,
			autoplayTimeout: 3000,
			autoplayHoverPause: true
			});
		},
		destroyCarousel() {
			const $carousel = $('.owl-carousel');
			if ($carousel.hasClass('owl-loaded')) {
				$carousel.trigger('destroy.owl.carousel');
				$carousel.removeClass('owl-loaded'); // Eliminar clase de estado
				
			}
			// $('.owl-carousel').owlCarousel('destroy');
		}
	}

}
</script>

<style scoped>

.trans_200 {
	-webkit-transition: all 200ms ease;
	-moz-transition: all 200ms ease;
	-ms-transition: all 200ms ease;
	-o-transition: all 200ms ease;
	transition: all 200ms ease;
}

/*********************************
5. Home
*********************************/

.home {
	width: 100%;
}

/*********************************
5.1 Hero Slider
*********************************/

.hero_slider_container {
	width: 100%;
	height: 100%;
}

.hero_slide {
	width: 100%;
	height: 100%;
}

.hero_slide_background {
    /*background-image:url(../../../assets/img/slider_background.jpg);*/
	background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
	url(../../../assets/img/slider_background.jpg);	
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-repeat: no-repeat;
	background-size: cover;
	background-position: center center;
}

.hero_slide_container {
	width: 100%;
	height: 100vh;
}

.hero_slide_content {
	max-width: 80%;
	-webkit-transform: translateY(30px);
	-moz-transform: translateY(30px);
	-ms-transform: translateY(30px);
	-o-transform: translateY(30px);
	transform: translateY(30px);
}

.hero_slide_content h1 {
	font-size: 72px;
	font-weight: 400;
	color: #FFFFFF;
}

.hero_slide_content h1 span {
	background: #ffb606;
	padding-left: 13px;
	padding-right: 13px;
	margin-left: -12px;
	margin-right: -12px;
}

.animated {
	-webkit-animation-duration: 1s !important;
	animation-duration: 1s !important;
	-webkit-animation-delay: 500ms;
	animation-delay: 500ms;
}

.animate-out {
	-webkit-animation-delay: 0ms;
	animation-delay: 0ms;
}

/*********************************
5.2 Hero Slider Navigation
*********************************/

.hero_slider_nav {
	display: -webkit-box;
	display: -moz-box;
	display: -ms-flexbox;
	display: -webkit-flex;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	position: absolute;
	top: 50%;
	-webkit-transform: translateY(-50%);
	-moz-transform: translateY(-50%);
	-ms-transform: translateY(-50%);
	-o-transform: translateY(-50%);
	transform: translateY(calc(-50% + 30px));
	width: 58px;
	height: 58px;
	background: #FFFFFF;
	z-index: 9;
	cursor: pointer;
}

.hero_slider_nav:hover {
	background: #ffb606;
}

.hero_slider_nav:hover span {
	color: #FFFFFF;
}

.hero_slider_nav span {
	display: block;
	text-transform: uppercase;
	font-size: 12px;
	font-weight: 700;
	color: #121212;
	line-height: 1;
}

.hero_slider_left {
	left: 4.32%;
}

.hero_slider_right {
	right: 4.32%;
}

/*********************************
6. Hero Boxes
*********************************/

.hero_boxes {
	width: 100%;
	height: 0px;
	z-index: 9;
	padding-top: 0px;
}

.hero_boxes_inner {
	position: absolute;
	top: -212px;
	left: 0;
	width: 100%;
}

.hero_box {
	width: 100%;
	height: 161px;
	background: #1a1a1a;
	padding-left: 50px;
	cursor: pointer;
}

.hero_box:hover {
	background: #ffb606;
}

.hero_box img {
	width: 62px;
	height: auto;
	margin-top: -6px;
}

.svg path {
	fill: #ffb606;
}

.hero_box svg {
	width: 62px;
	height: auto;
}

.hero_box:hover svg path {
	fill: #FFFFFF;
}

.hero_box_content {
	padding-left: 13px;
	padding-top: 11px;
	margin-top: -6px;
}

.hero_box_title {
	font-size: 24px;
	font-weight: 500;
	color: #FFFFFF;
	margin-bottom: 7px;
}

.hero_box_link {
	font-size: 12px;
	font-weight: 500;
	text-transform: uppercase;
	color: #FFFFFF;
	padding-left: 3px;
}

.hero_box_link:hover {
	color: #1a1a1a;
}


@media only screen and (max-width: 1280px)
{

	.hero_slide_content h1
	{
		font-size: 56px;
	}
	
}

@media only screen and (max-width: 1199px)
{
	.hero_box
	{
		padding-left: 20px;
	}
}

@media only screen and (max-width: 991px)
{
	
	.hero_slide_content h1
	{
		font-size: 48px;
	}
	.hero_boxes
	{
		width: 100%;
		height: auto;
		padding-top: 117px;
	}
	.hero_boxes_inner
	{
		position: relative;
		top: auto;
		left: auto;
	}
	.hero_box
	{
		padding-left: 50px;
	}
	.hero_box_col
	{
		margin-bottom: 30px;
	}
	.hero_box_col:last-child
	{
		margin-bottom: 0px;
	}
}


@media only screen and (max-width: 575px)
{
	.hero_slider_nav
	{
		display: none;
	}
	.hero_slide_content
	{
		max-width: 100%;
		padding-left: 15px;
		padding-right: 15px;
	}
}


@media only screen and (max-width: 479px)
{
	
	.hero_slide_content h1
	{
		font-size: 28px;
	}
	.hero_slide_content h1 span
	{
		padding-left: 5px;
		padding-right: 5px;
		margin-left: 0px;
		margin-right: 0px;
	}
	.hero_boxes
	{
		padding-top: 80px;
	}
	.hero_box
	{
		padding-left: 15px;
		height: 120px;
	}
	.hero_box_content
	{
		padding-top: 6px;
	}
	.hero_box img
	{
		width: 45px;
	}
	.hero_box_title
	{
		font-size: 18px;
		margin-bottom: 3px;
	}
	.hero_box_link
	{
		font-size: 10px;
	}
}
</style>