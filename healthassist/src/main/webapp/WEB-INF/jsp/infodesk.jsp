<!DOCTYPE HTML>
<html>
<head>
<title>PulmoPal by The Voyagers</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<link href='http://fonts.googleapis.com/css?family=Oxygen:400,300,700'
	rel='stylesheet' type='text/css'>
<script
	src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="/meta/js/nfo/skel.min.js"></script>
<script src="/meta/js/nfo/skel-panels.min.js"></script>
<script src="/meta/js/nfo/init.js"></script>
<noscript>
	<link rel="stylesheet" href="/meta/css/nfo/skel-noscript.css" />
	<link rel="stylesheet" href="/meta/css/nfo/style.css" />
</noscript>
</head>
<body class="homepage">

	<div id="header">
		<div class="container">

			<div id="logo">
				<h1>
					<a href="#">PulmoPal</a>
				</h1>
			</div>

			<nav id="nav">
				<ul>
					<li class="active"><a href="info.jsp">Infodesk</a></li>
				</ul>
			</nav>

		</div>
	</div>

	<div id="main">
		<div class="container">
			<header>
				<h2>Trending videos</h2>
			</header>
			<div class="row">
				<div class="3u">
					<section>
						<iframe width="284" height="160"
							src="https://www.youtube.com/embed/i0ZabxXmH4Y" frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
							allowfullscreen></iframe>
						<p>Coronavirus disease (COVID-19) by World Health Organization
							(WHO)</p>
						<a href="https://www.youtube.com/watch?v=i0ZabxXmH4Y"
							class="button">Watch on YouTube</a>
					</section>
				</div>
				<div class="3u">
					<section>
						<iframe width="284" height="160"
							src="https://www.youtube.com/embed/rNnA9bQ9EJE" frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
							allowfullscreen></iframe>
						<p>COVID-19: Facts & Myths | Coronavirus MythBusters by Practo</p>
						<a href="https://www.youtube.com/watch?v=rNnA9bQ9EJE"
							class="button">Watch on YouTube</a>
					</section>
				</div>
				<div class="3u">
					<section>
						<iframe width="284" height="160"
							src="https://www.youtube.com/embed/O1TiRp-lPC4" frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
							allowfullscreen></iframe>
						<p>The Difference Between Bronchitis and Pneumonia by Lee
							Health</p>
						<a href="https://www.youtube.com/watch?v=O1TiRp-lPC4"
							class="button">Watch on YouTube</a>
					</section>
				</div>
				<div class="3u">
					<section>
						<iframe width="284" height="160"
							src="https://www.youtube.com/embed/eJppC_W_LnQ" frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
							allowfullscreen></iframe>
						<p>Is pneumonia bacterial or viral? by Mayo Clinic</p>
						<a href="https://www.youtube.com/watch?v=eJppC_W_LnQ"
							class="button">Watch on YouTube</a>
					</section>
				</div>
			</div>
			<div class="divider">&nbsp;</div>
			<div class="row">

				<div class="8u skel-cell-important">
					<section id="content">
						<header>
							<h2>6 Tips for Protecting Your Lungs</h2>
							<span class="byline">copdnewstoday.com</span>
						</header>
						<p>
							<a href="#" class="image full"><img
								src="/meta/images/nfo/pics02.png" alt=""></a>
						</p>
						<p>"We only get one set of lungs so it's imperative that we
							look after them."</p>
						<a
							href="https://copdnewstoday.com/2017/03/06/6-tips-protecting-lungs/"
							class="button">Read More</a>
					</section>
				</div>

				<div id="sidebar" class="4u">
					<section>
						<header>
							<h2>Useful articles</h2>
							<span class="byline">Curated by PulmoPal Staff</span>
						</header>
						<p>Authors: American Lung Association | WebMD | The Centre for
							Evidence-Based Medicine | British Lung Foundation | RT Magazine</p>
						<ul class="default">
							<li><a
								href="https://www.lung.org/lung-health-diseases/lung-disease-lookup/covid-19/about-covid-19">Learn
									About COVID-19</a></li>
							<li><a
								href="https://www.webmd.com/lung/what-does-covid-do-to-your-lungs#1">What
									Does COVID-19 Do to Your Lungs?</a></li>
							<li><a
								href="https://www.webmd.com/lung/covid-and-pneumonia#1">Coronavirus
									and Pneumonia</a></li>
							<li><a
								href="https://www.cebm.net/covid-19/differentiating-viral-from-bacterial-pneumonia/">Differentiating
									viral from bacterial pneumonia</a></li>
							<li><a href="https://www.blf.org.uk/support-for-you/carers">Caring
									for someone with a lung condition</a></li>
							<li><a
								href="https://rtmagazine.com/disorders-diseases/chronic-pulmonary-disorders/asthma/consider-respiratory-related-charities-holidays/">Respiratory-related
									Charities</a></li>
						</ul>
					</section>
				</div>

			</div>

		</div>
	</div>

	<div id="footer">
		<div class="container">
			<div align="center">
				<h1>PulmoQuiz</h1>
				<div class="quiz-container">
					<div id="quiz"></div>
				</div>
				<button id="previous">Previous Question</button>
				<button id="next">Next Question</button>
				<button id="submit">Submit Quiz</button>
				<div id="results"></div>
			</div>
		</div>
	</div>

	<div id="copyright">
		<div class="container">
			&copy 2020 <a href="#">The Voyagers</a>
		</div>
	</div>

	<script>(function () {

        function buildQuiz() {

            const output = [];

            myQuestions.forEach(
                (currentQuestion, questionNumber) => {

                    const answers = [];

                    for (letter in currentQuestion.answers) {

                        answers.push(
                            `<label>
                <input type="radio" name="question\${questionNumber}" value="\${letter}">
                \${letter} :
                \${currentQuestion.answers[letter]}
              </label>`
                        );
                    }

                    output.push(
                        `<div class="slide">
              <div class="question"> \${currentQuestion.question} </div>
              <div class="answers"> \${answers.join("")} </div>
            </div>`
                    );
                }
            );
            
            quizContainer.innerHTML = output.join('');
        }

        function showResults() {

            const answerContainers = quizContainer.querySelectorAll('.answers');

            let numCorrect = 0;

            myQuestions.forEach((currentQuestion, questionNumber) => {

                const answerContainer = answerContainers[questionNumber];
                const selector = `input[name=question\${questionNumber}]:checked`;
                const userAnswer = (answerContainer.querySelector(selector) || {}).value;

                if (userAnswer === currentQuestion.correctAnswer) {
                    numCorrect++;
                    answerContainers[questionNumber].style.color = 'lightgreen';
                }
                else {
                    answerContainers[questionNumber].style.color = 'red';
                }
            });
            resultsContainer.innerHTML = `\${numCorrect} out of \${myQuestions.length}`;
        }

        function showSlide(n) {
            slides[currentSlide].classList.remove('active-slide');
            slides[n].classList.add('active-slide');
            currentSlide = n;
            if (currentSlide === 0) {
                previousButton.style.display = 'none';
            }
            else {
                previousButton.style.display = 'inline-block';
            }
            if (currentSlide === slides.length - 1) {
                nextButton.style.display = 'none';
                submitButton.style.display = 'inline-block';
            }
            else {
                nextButton.style.display = 'inline-block';
                submitButton.style.display = 'none';
            }
        }

        function showNextSlide() {
            showSlide(currentSlide + 1);
        }

        function showPreviousSlide() {
            showSlide(currentSlide - 1);
        }

        const quizContainer = document.getElementById('quiz');
        const resultsContainer = document.getElementById('results');
        const submitButton = document.getElementById('submit');
        const myQuestions = [
        	{
                question: "____ is not good for your lungs.",
                answers: {
                    a: "Exercising",
                    b: "Smoking",
                    c: "Singing"
                },
                correctAnswer: "b"
            },
            {
                question: "As you age, your lungs hold less air.",
                answers: {
                    a: "True",
                    b: "False"
                },
                correctAnswer: "a"
            },
            {
                question: "Pneumonia is an infection that fills your lungs with:",
                answers: {
                    a: "Carbon dioxide",
                    b: "Blood",
                    c: "Fluid"
                },
                correctAnswer: "c"
            },
            {
                question: "You get asthma and bronchitis in your:",
                answers: {
                    a: "Airways",
                    b: "Lungs",
                    c: "Diaphragm"
                },
                correctAnswer: "a"
            },
            {
                question: "How does weather seem to affect the novel coronavirus?",
                answers: {
                    a: "The virus can't survive in hot, humid climates.",
                    b: "Cold temperatures can kill the virus.",
                    c: "It is not yet known."
                },
                correctAnswer: "c"
            },
            {
                question: "A vaccine stimulates your immune system to produce antibodies, like it would if you were exposed to the virus.",
                answers: {
                    a: "True",
                    b: "False"
                },
                correctAnswer: "a"
            }
        ];

        buildQuiz();

        const previousButton = document.getElementById("previous");
        const nextButton = document.getElementById("next");
        const slides = document.querySelectorAll(".slide");
        let currentSlide = 0;

        showSlide(currentSlide);

        submitButton.addEventListener('click', showResults);
        previousButton.addEventListener("click", showPreviousSlide);
        nextButton.addEventListener("click", showNextSlide);
    })();</script>

</body>
</html>