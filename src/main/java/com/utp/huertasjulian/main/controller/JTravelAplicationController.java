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

   
    

   


    
}
