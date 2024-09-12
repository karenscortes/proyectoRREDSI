<template>
    <!-- Footer -->
    <footer class="footer mt-3">
        <div class="container">
            <!-- Footer Content -->

            <div class="footer_content">
                <div class="row">

                    <!-- Footer Column - About -->
                    <div class="col-lg-3 footer_col">

                        <!-- Logo -->
                        <div class="logo_container">
                            <div class="logo">
                                <img src="../../assets/img/logoRredsi.png" alt="">
                                <span>RREDSI</span>
                            </div>
                        </div>

                        <p class="footer_about_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla.</p>

                    </div>

                    <!-- Footer Column - Menu -->

                    <div class="col-lg-3 footer_col">
                        <div class="footer_column_title">Menú</div>
                        <div class="footer_column_content">
                            <ul>
                                <li class="footer_list_item"><a href="#">Inicio</a></li>
                                <li class="footer_list_item"><a href="#">Proyectos</a></li>
                                <li class="footer_list_item"><a href="courses.html">Evaluadores</a></li>
                                <li class="footer_list_item"><a href="news.html">Login</a></li>
                                <li class="footer_list_item"><a href="contact.html">Contáctanos</a></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Footer Column - Usefull Links -->

                    <div class="col-lg-3 footer_col">
                        <div class="footer_column_title">Links útiles</div>
                        <div class="footer_column_content">
                            <ul>
                                <li class="footer_list_item"><a href="#">Proyectos</a></li>
                                <li class="footer_list_item"><a href="#">RREDSI</a></li>
                                <li class="footer_list_item"><a href="#">Contáctos</a></li>
                                <li class="footer_list_item"><a href="#">Encuentros regionales</a></li>
                                <li class="footer_list_item"><a href="#">Encuentros departamentales</a></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Footer Column - Contact -->

                    <div class="col-lg-3 footer_col">
                        <div class="footer_column_title">Contácto</div>
                        <div class="footer_column_content">
                            <ul>
                                <li class="footer_contact_item">
                                    <div class="footer_contact_icon">
                                        <img src="../../assets/img/placeholder.svg"
                                            alt="https://www.flaticon.com/authors/lucy-g">
                                    </div>
                                    Universidad tecnológica de Pereira
                                </li>
                                <li class="footer_contact_item">
                                    <div class="footer_contact_icon">
                                        <img src="../../assets/img/smartphone.svg"
                                            alt="https://www.flaticon.com/authors/lucy-g">
                                    </div>
                                    +57 3104289839
                                </li>
                                <li class="footer_contact_item">
                                    <div class="footer_contact_icon">
                                        <img src="../../assets/img/envelope.svg"
                                            alt="https://www.flaticon.com/authors/lucy-g">
                                    </div>crredsi@gmail.com
                                </li>
                            </ul>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Footer Copyright -->

            <div class="footer_bar d-flex flex-column flex-sm-row align-items-center">
                <div class="footer_copyright">
                    <span><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                        Copyright &copy; {{ currentYear }} All rights reserved | This template is made with by
                        <a href="#" target="_blank">ADSO 2670586</a>
                        <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                    </span>
                </div>
                <div class="footer_social ml-sm-auto">
                    <ul class="menu_social">

                        <li class="menu_social_item"><a href="https://www.instagram.com/rredsiquindio/"><i
                                    class="fab fa-instagram"></i></a></li>
                        <li class="menu_social_item"><a href="https://www.facebook.com/rredsi?mibextid=ZbWKwL"><i
                                    class="fab fa-facebook-f"></i></a></li>
                        <li class="menu_social_item"><a href="https://x.com/Rredsi"><i class="fab fa-twitter"></i></a>
                        </li>
                    </ul>
                </div>
            </div>

        </div>
    </footer>

</template>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear(),
    };
  },
};
</script>

<style>
    /*********************************
15. Footer
*********************************/

.footer {
	width: 100%;
	padding-top: 0px;
	background: #1a1a1a;
}

.footer .section_title h1 {
	color: #FFFFFF;
}

/*********************************
15.1 Newsletter
*********************************/

.newsletter {

	padding-bottom: 85px;
	border-bottom: solid 2px #4d4e4e;
}

.newsletter_form_container {
	width: 60%;
	margin-top: 48px;
}

.newsletter_email {
	width: calc(100% - 164px);
	height: 42px;
	border: none;
	padding-left: 27px;
	font-weight: 500;
	color: #1a1a1a;
}

.newsletter_email:focus {
	outline: solid 2px #ffb606;
}

.newsletter_submit_btn {
	width: 164px;
	height: 42px;
	border: none;
	background: #ffb606;
	color: #FFFFFF;
	font-size: 14px;
	font-weight: 500;
	cursor: pointer;
}

.newsletter_submit_btn:focus {
	border: solid 2px #FFFFFF;
}

/*********************************
15.2 Footer Content
*********************************/

.footer_content {
	padding-top: 80px;
	padding-bottom: 83px;
	border-bottom: solid 2px #4d4e4e;
}

.footer_content .logo_container {
	padding-left: 0px;
}

.footer_content .logo span {
	color: #FFFFFF;
}

.footer_about_text {
	margin-top: 24px;
	margin-bottom: 0px;
	padding-right: 20px;
}

.footer_column_title {
	font-size: 18px;
	font-weight: 500;
	color: #FFFFFF;
	padding-top: 15px;
}

.footer_column_content {
	margin-top: 32px;
}

.footer_list_item {
	margin-bottom: 11px;
}

.footer_list_item a {
	font-size: 14px;
	color: #a5a5a5;
	-webkit-transition: all 200ms ease;
	-moz-transition: all 200ms ease;
	-ms-transition: all 200ms ease;
	-o-transition: all 200ms ease;
	transition: all 200ms ease;
}

.footer_list_item a:hover {
	color: #ffb606;
}

.footer_contact_item {
	font-size: 14px;
	font-weight: 400;
	color: #a5a5a5;
	margin-bottom: 22px;
}

.footer_contact_item:last-child {
	margin-bottom: 0px;
}

.footer_contact_icon {
	display: inline-block;
	width: 24px;
	height: 24px;
	vertical-align: middle;
	margin-right: 10px;
}

.footer_contact_icon img {
	width: 100%;
}

/*********************************
15.3 Footer Copyright
*********************************/

.footer_bar {
	padding-top: 19px;
	padding-bottom: 19px;
}

.footer_social .menu_social_item a i {
	color: #FFFFFF;
}

.footer_social .menu_social_item a i:hover {
	color: #ffb606;
}

.footer_social .menu_social_item:last-child {
	margin-right: 0px;
}

.scroll-div {
	width: 1000px;
	height: 400px;
	overflow-y: auto;
	overflow-x: hidden;
}

body {
	font-family: Arial, sans-serif;
	margin: 20px;
	background-color: #f7f7f7;
}

.form-section {
	background-color: #f8f9fa;
	border: 1px solid #ced4da;
	padding: 20px;
	border-radius: 5px;
	max-width: 800px;
	margin: auto;
}

.form-section h2 {
	color: rgb(255, 182, 6);
	text-align: center;
}

.form-section .title-icon {
	color: rgb(255, 182, 6);
	margin-right: 10px;
	font-size: 1.5rem;
	margin-bottom: 10px;
}

.title-line {
	border-top: 2px solid rgb(255, 182, 6);
	margin-top: -10px;
}

.btn{
	background-color: rgb(255, 182, 6);
}

.btn:hover {
	box-shadow: none;
    color: #494949;
	background-color: rgb(255, 182, 6);
}

.accordion-button:focus{
	box-shadow: none;
	background-color: rgb(255, 182, 6);
	outline: none;
}

.span_acor{
	font-size: 18px
}

.modal-header .icon {
	color:rgb(255, 182, 6);
	font-size: 2rem;
	margin-right: 10px;
}

.modal-header{
	color: #000000;
	font-size: 2rem;
	margin-right: 10px;
}

.enlace{
	padding: 0.6rem;
	text-decoration: none;
	text-align: center;
	color: black;
	transition: all 0.4s ease-in-out;
}

.enlace:focus{
	background-color: rgb(255, 182, 6);
	color: black;
}

#cont_consultarProyecto{
	scroll-margin-top: 104px;
}

.botonAbrir{
	width: 30%;
	font-size: 18px;
}

.w-30{
	width: 30% !important;
}

.btn-custom {
	display: inline-flex;
	align-items: center;
	padding: 0.5rem 1rem;
	border: 1px solid transparent;
	border-radius: 0.375rem; 
	font-size: 1rem;
	text-align: center;
	text-decoration: none;
	background-color: rgb(255, 182, 6); 
	color: black;
}

.btn-custom:hover {
	background-color: #e0a800;
	color: black;
}

.btn-custom i {
	margin-right: 0.5rem; 
}
</style>
