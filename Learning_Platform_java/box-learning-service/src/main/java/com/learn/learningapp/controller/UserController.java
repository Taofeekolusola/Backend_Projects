package com.learn.learningapp.controller;

import com.learn.learningapp.model.User;
import com.learn.learningapp.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
import java.util.List;
@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    // Register a new user

    @PostMapping("/register")
    public User registerUser(@RequestBody User user) {
        return userService.registerUser(user);
    }

    // Login endpoint (simplified)
    @PostMapping("/login")
    public String loginUser(@RequestBody User loginDetails) {
        return userService.loginUser(loginDetails);
    }
    
     // Get all users
     @GetMapping("/")
     public List<User> getAllUsers() {
         return userService.getAllUsers();
     }
 
     // Get user by ID
     @GetMapping("/{id}")
     public Optional<User> getUserById(@PathVariable Long id) {
         return userService.getUserById(id);
     }

     // Update a user (PUT)
    @PutMapping("/{id}")
    public String updateUser(@PathVariable Long id, @RequestBody User userDetails) {
        boolean updated = userService.updateUser(id, userDetails);
        if (updated) {
            return "User updated successfully!";
        } else {
            return "User not found!";
        }
    }

    // Delete a user (DELETE)
    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable Long id) {
        boolean deleted = userService.deleteUser(id);
        if (deleted) {
            return "User deleted successfully!";
        } else {
            return "User not found!";
        }
    }
}