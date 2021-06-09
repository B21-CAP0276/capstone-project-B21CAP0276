package com.febrina.vcsapp.data

//import com.pusher.rest.Pusher
//import org.springframework.http.ResponseEntity
//import org.springframework.web.bind.annotation.*
//
//@RestController
//@RequestMapping("/message")
//class MessageController {
//    private val pusher = Pusher("1213924", "a13e9b303d1a096e8d7f", "2da2c3e6ac5891f8f137")
//
//    init {
//        pusher.setCluster("ap1")
//    }
//
//    @PostMapping
//    fun postMessage(@RequestBody message: Message) : ResponseEntity<Unit> {
//        pusher.trigger("chat", "new_message", message)
//        return ResponseEntity.ok().build()
//    }
//}