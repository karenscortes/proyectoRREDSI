<template>
    <!-- header -->
    <header class="header d-flex flex-grow position-absolute top-0 w-80">
        <div class="header_content with_button d-flex flex-row align-items-center justify-content-start">
            <!-- Logo -->
            <div class="logo_container">
                <div class="logo">
                    <img class="img-fluid" src="../plantilla/images/logoRredsi.png" alt="">
                    <span>RREDSI</span>
                </div>
            </div>

            <!-- Main Navigation -->
            <nav class="main_nav_container flex-grow-1">
                <div class="main_nav">
                    <ul class="main_nav_list d-flex justify-content-between">
                        <li class="main_nav_item"><a href="principal.html">Inicio</a></li>
                        <li class="main_nav_item"><a href="perfil.html">Perfil</a></li>
                        <li class="main_nav_item">
                            <div class="dropdown">
                                <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                    aria-expanded="false">
                                    Evaluadores
                                </a>
                                <div class="dropdown-menu text-center">
                                    <a href="postulaciones.html">Postulaciones</a><br>
                                    <a href="lista_evaluadores.html">Lista de Evaluadores</a>
                                </div>
                            </div>
                        </li>
                        <li class="main_nav_item">
                            <div class="dropdown">
                                <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                    aria-expanded="false">
                                    Proyectos
                                </a>
                                <div class="dropdown-menu text-center">
                                    <a href="#">Asignación de <br> Proyectos</a><br>
                                    <a href="lista_proyectos.html">Lista de Proyectos</a>
                                </div>
                            </div>
                        </li>
                        <li class="main_nav_item">
                            <div class="dropdown">
                                <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                    aria-expanded="false">
                                    Evento
                                </a>
                                <div class="dropdown-menu text-center">
                                    <a href="salas.html">Salas</a><br>
                                    <a href="asistencia.html">Asistencia</a>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
        <a href="#" class="header_side d-flex flex-row justify-content-center align-items-center">
            <h3 class="main_nav_item text-dark">Cerrar sesión</h3>
        </a>

        <!-- Hamburger -->
        <div class="hamburger_container">
            <i class="fas fa-bars trans_200"></i>
        </div>

    </header>
    <!-- fondo del header -->
    <div class="home">
        <div class="home_background_container prlx_parent">
            <div class="home_background prlx" style="background-image:url(../plantilla/images/teachers_background.jpg)"></div>
        </div>
    
    </div>
    <!-- Menu -->
    <div class="menu_container menu_mm">

        <!-- Menu Close Button -->
        <div class="menu_close_container">
            <div class="menu_close"></div>
        </div>

        <!-- Menu Items -->
        <div class="menu_inner menu_mm">
            <div class="menu menu_mm">
                <ul class="menu_list menu_mm">
                    <li class="menu_item menu_mm"><a href="principal.html">Inicio</a></li>
                    <li class="menu_item menu_mm"><a href="#">Perfil</a></li>
                    <li class="menu_item menu_mm">
                        <div class="dropdown">
                            <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                aria-expanded="false">
                                Evaluadores
                            </a>
                            <div class="dropdown-menu text-center">
                                <a href="#">Postulaciones</a><br>
                                <a href="lista_evaluadores.html">Lista de Evaluadores</a>
                            </div>
                        </div>
                    </li>
                    <li class="menu_item menu_mm">
                        <div class="dropdown">
                            <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                aria-expanded="false">
                                Proyectos
                            </a>
                            <div class="dropdown-menu text-center">
                                <a href="#">Asignación de <br> Proyectos</a><br>
                                <a href="lista_proyectos.html">Lista de Proyectos</a>
                            </div>
                        </div>
                    </li>
                    <li class="menu_item menu_mm">
                        <div class="dropdown">
                            <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                aria-expanded="false">
                                Evento
                            </a>
                            <div class="dropdown-menu text-center">
                                <a href="salas.html">Salas</a><br>
                                <a href="#">Asistencia</a>
                            </div>
                        </div>
                    </li>
                    <li class="menu_item menu_mm"><a href="#">Cerrar sesión</a></li>
                </ul>

                <!-- Menu Social -->

                <div class="menu_social_container menu_mm">
                    <ul class="menu_social menu_mm">
                        <li class="menu_social_item menu_mm"><a href="https://www.instagram.com/rredsiquindio/"><i
                                    class="fab fa-instagram"></i></a></li>
                        <li class="menu_social_item menu_mm"><a
                                href="https://www.facebook.com/rredsi?mibextid=ZbWKwL"><i
                                    class="fab fa-facebook-f"></i></a></li>
                        <li class="menu_social_item menu_mm"><a href="https://x.com/Rredsi"><i
                                    class="fab fa-twitter"></i></a></li>
                    </ul>
                </div>

                <div class="menu_copyright menu_mm">ADSO 2670586 All rights reserved</div>
            </div>

        </div>

    </div>
</template>