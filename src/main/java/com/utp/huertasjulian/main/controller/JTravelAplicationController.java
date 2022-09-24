package com.utp.huertasjulian.main.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class JTravelAplicationController {
    
    @GetMapping("/")
    public String goToIndex(){
        return "index";
    }

    @GetMapping("/index.html")
    public  String goToInicio(){
        return goToIndex();
    }

    @GetMapping("/browse.html")
    public String goToBrowse(){
        return "browse";
    }

    @GetMapping("/details.html")
    public String goToDetails(){
        return "details";
    }

    @GetMapping("/profile.html")
    public String goToProfile(){
        return "profile";
    }

    @GetMapping("/streams.html")
    public String goToStreams(){
        return "streams";
    }

    @GetMapping("/login.html")
    public String goToLogin(){
        return "login";
    }

   
    

   


    
}
