package com.cerner.shipit.voyagers.healthassist.service;

import java.io.File;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.FileSystemResource;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

	public static final String FROM_ADDR = "noreply@voyagers.com";

	private static final String HEAT_MAP_SUBJECT = "PulmoPal: Chest X-Ray Heat Map";

	private static final String HEAT_MAP_CONTENT_FORMAT = "Hi %s,\n\n%s\nPlease find the heat map "
			+ "based on your CXR attached to this email.\n\nRegards,\n\nThe Voyagers";

	private JavaMailSender javaMailSender;

	@Autowired
	public EmailService(JavaMailSender javaMailSender) {
		this.javaMailSender = javaMailSender;
	}

	public void sendHeatMap(String diagnosis, String recipientAddress, String recipientName, String recipient, String... pathToAttachments)
			throws MessagingException {
		
		MimeMessage mimeMessage = javaMailSender.createMimeMessage();

		MimeMessageHelper mimeMessageHelper = new MimeMessageHelper(mimeMessage, true);

		mimeMessageHelper.setFrom(FROM_ADDR);
		mimeMessageHelper.setTo(recipientAddress);
		mimeMessageHelper.setSubject(HEAT_MAP_SUBJECT);
		if(recipient.equals("Doctor")) {
			if(!recipientName.contains("Dr.")) {
				recipientName = "Dr. " + recipientName; 
			}
		}
		
		if(!diagnosis.equals("Normal")) {
			mimeMessageHelper.setText(String.format(HEAT_MAP_CONTENT_FORMAT, recipientName, "DIAGNOSIS : Suspected " + diagnosis));
		} else {
			mimeMessageHelper.setText(String.format(HEAT_MAP_CONTENT_FORMAT, recipientName, "DIAGNOSIS : No anomaly related to Covid or Pneumonia"));
		}

		if( pathToAttachments.length > 1 ) {
			FileSystemResource fileSystemResource = new FileSystemResource(new File(pathToAttachments[0]));
			mimeMessageHelper.addAttachment("Original.jpg", fileSystemResource);
			fileSystemResource = new FileSystemResource(new File(pathToAttachments[1]));
			mimeMessageHelper.addAttachment("HeatMap.jpg", fileSystemResource);
		} else {
			FileSystemResource fileSystemResource = new FileSystemResource(new File(pathToAttachments[0]));
			mimeMessageHelper.addAttachment("HeatMap.jpg", fileSystemResource);
		}
		
		javaMailSender.send(mimeMessage);
		System.out.println("Email sent!");
	}
}
