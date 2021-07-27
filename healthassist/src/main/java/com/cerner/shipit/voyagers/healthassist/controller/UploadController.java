package com.cerner.shipit.voyagers.healthassist.controller;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.mail.MessagingException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.cerner.shipit.voyagers.healthassist.service.EmailService;

@Controller
public class UploadController {

	private static final String UPLOADED_FOLDER = "C:\\ShipItVIITemp\\";

	private static final String PATH_TO_ATTACHMENT = "C:\\ShipItVII\\Analysis\\heatmap.jpeg";

	private EmailService emailService;

	@Autowired
	public UploadController(EmailService emailService) {
		this.emailService = emailService;
	}

	@GetMapping("/")
	public String index() {
		return "index";
	}

	@PostMapping("/upload")
	@ResponseBody
	public String singleFileUpload(@RequestParam("file") MultipartFile file) {

		System.out.println("UPLOADED FILE NAME : " + file.getOriginalFilename());

		if (file.isEmpty()) {
			return "emptyFile";
		}

		try {

			// Get the file and save it somewhere
			byte[] bytes = file.getBytes();

			if (!(new File(UPLOADED_FOLDER)).exists()) {
				(new File(UPLOADED_FOLDER)).mkdirs();
			}

			Path path = Paths.get(UPLOADED_FOLDER + file.getOriginalFilename());
			Files.write(path, bytes);

		} catch (IOException e) {
			e.printStackTrace();
		}

		return "File Uploaded : " + file.getOriginalFilename();
	}

	@GetMapping("/uploadStatus")
	public String uploadStatus() {
		return "uploadStatus";
	}

	@PostMapping("/sendEmail")
	@ResponseBody
	public String sendHeatMapEmail(@RequestParam("recipientAddress") String recipientAddress,
			@RequestParam("recipientName") String recipientName, @RequestParam("recipient") String recipient, @RequestParam("fileName") String fileName, @RequestParam("diagnosis") String diagnosis) throws MessagingException {
		
		if(recipient.equals("Self")) {
			emailService.sendHeatMap(diagnosis, recipientAddress, recipientName, recipient, PATH_TO_ATTACHMENT);
		} else if(recipient.equals("Doctor")) {
			emailService.sendHeatMap(diagnosis, recipientAddress, recipientName, recipient, UPLOADED_FOLDER + fileName, PATH_TO_ATTACHMENT);
		}

		return "Email Sent!";
	}

	@GetMapping("/infodesk")
	public String infodesk() {
		return "infodesk";
	}
}