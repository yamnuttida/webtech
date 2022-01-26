<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Portfolio</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">
    <style>
    body {
    margin: 0;
    padding: 0;
    font-family: 'Montserrat', sans-serif;
}

.clearfix {
    clear: both;
}

.container {
    width: 1100px;
    margin: 0 auto;
}

.menubar {
    width: 100%;
    height: 60px;
    background: #fff;
    box-shadow: 0 0 10px #666; 
}

.menubar .logo {
    float: left;
}

.menubar h1 {
    margin: 0;
    font-size: 30px;
    font-weight: normal;
    padding: 10px;
}
.menubar ul.menu {
    list-style: none;
    float: right;
}
.menubar ul.menu li {
    float: left;
    margin-right: 20px;
}
.menubar ul.menu li a {
    text-decoration: none;
    color: #333;
    border-bottom: 2px solid transparent;
    padding-bottom: 20px;
    transition: all 0.2s ease;
}
.menubar ul.menu li a:hover {
    border-bottom: 2px solid #333;
    padding-bottom: 0;
}

.info1 {
    width: 100%;
    height: 400px;
}
.info1_area {
    color: #333;
}
.info1_area img {
    margin-top: 80px;
    float: left;
}
.info1_text {
    text-align: center;
    width: 460px;
    float: left;
    margin-left: 70px;
    margin-top: 140px;
}
.info1_area h1 {
    margin: 0;
    font-weight: normal;
}

.contact {
    width: 100%;
    height: 515px;
}

.contact_area h1 {
    font-weight: normal;
}
.contact_area input {
    margin: 10px 0;
    border: 2px solid #333;
    width: 350px;
    padding: 10px;
}

.contact_area textarea {
    margin: 10px 0;
    border: 2px solid #333;
    width: 350px;
    padding: 10px;
}

.contact_area button {
    padding: 10px;
    width: 90px;
    background: #333;
    color: #fff;
    border: 2px solid transparent;
    text-transform: uppercase;
    transition: all 0.3s ease;
    cursor: pointer;
}
.contact_area button:hover {
    background: #fff;
    color: #333;
    border: 2px solid #333;
}




footer {
    background: #333;
    margin-top: 60px;
    padding: 20px;
    text-align: center;
    color: #fff;
}
footer p {
    margin: 0;
}
    </style>


</head>
<body>

    <div class="menubar">
        <div class="container">
            <div class="logo">
                <h1>TANGMAY</h1>
            </div>
            <ul class="menu">
                <li>
                    <a href="index.html">Home</a>
                </li>
                <li>
                    <a href="index1.html">YAMMIE</a>
                </li>
                <li>
                    <a href="">TANGMAY</a>
                </li>
            </ul>
        </div>
    </div>

    <div class="clearfix"></div>

    <section class="info1">
        <div class="container">
            <div class="info1_area">
                <a href="https://www.facebook.com/profile.php?id=100004960632598" target="_blank">
                <img src="tm.jpg" alt="" width = "350">                
                </a>
                
                <div class="info1_text">
                    <h2>I'M TANGMAY</h2>
                    <h1>ARTHITAYA CHOMTHONG</h1>
                    <p> Birthday : 18/03/2001</p>   
                </div>

            </div>
            
        </div>
    </section>


    <footer>
        <p>Young | Data Sciencetists</p>
    </footer>
    
</body>
</html>