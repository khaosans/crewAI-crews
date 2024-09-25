import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { CheckCircle, Code, Database, Zap } from "lucide-react"

export default function LandingPage() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="px-4 lg:px-6 h-14 flex items-center">
        <Link className="flex items-center justify-center" href="#">
          <Zap className="h-6 w-6" />
          <span className="sr-only">AI Consulting</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#services">
            Services
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#case-studies">
            Case Studies
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#faq">
            FAQ
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#contact">
            Contact
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black text-white">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  AI is No Longer Just for Giants
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-300 md:text-xl">
                  Niche Solutions, Tailored to Your Unique Challenges
                </p>
              </div>
              <div className="w-full max-w-sm space-y-2">
                <form className="flex space-x-2">
                  <Input
                    className="max-w-lg flex-1 bg-gray-800 text-white border-gray-700"
                    placeholder="Enter your email"
                    type="email"
                  />
                  <Button type="submit">Book a Free Discovery Call</Button>
                </form>
                <p className="text-xs text-gray-400">
                  Get a Custom AI Solution Proposal. No commitment required.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              The Big Tech Era Left Niche Problems Unsolved. Now, It's Your Turn to Innovate.
            </h2>
            <p className="mt-4 max-w-[700px] text-gray-700 md:text-xl">
              Traditional tech development models favored startups focused on massive scale, leaving smaller industries
              out due to high costs or limited resources. But now, with AI empowering developers to do more, you don't
              need a massive budget or market size to get transformative solutions.
            </p>
          </div>
        </section>
        <section id="services" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              Custom AI, Blockchain, and Software Solutions for Your Industry
            </h2>
            <p className="mt-4 max-w-[700px] text-gray-700 md:text-xl">
              We specialize in designing tech solutions that are specifically crafted for your needs—whether you're in
              healthcare, agriculture, supply chain, or any other niche industry.
            </p>
            <ul className="mt-6 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              <li className="flex items-start space-x-4">
                <CheckCircle className="mt-1 h-5 w-5 text-green-500" />
                <div>
                  <h3 className="font-semibold">Tailored AI development for niche problems</h3>
                  <p className="text-sm text-gray-700">Customized AI solutions addressing your specific challenges</p>
                </div>
              </li>
              <li className="flex items-start space-x-4">
                <CheckCircle className="mt-1 h-5 w-5 text-green-500" />
                <div>
                  <h3 className="font-semibold">Blockchain solutions to improve transparency and efficiency</h3>
                  <p className="text-sm text-gray-700">Secure, decentralized systems for your business processes</p>
                </div>
              </li>
              <li className="flex items-start space-x-4">
                <CheckCircle className="mt-1 h-5 w-5 text-green-500" />
                <div>
                  <h3 className="font-semibold">Custom software solutions that don't require massive resources</h3>
                  <p className="text-sm text-gray-700">Efficient, scalable software tailored to your budget and needs</p>
                </div>
              </li>
            </ul>
          </div>
        </section>
        <section id="case-studies" className="w-full py-12 md:py-24 lg:py-32 bg-gray-100">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              See How We've Helped Companies Like Yours
            </h2>
            <div className="mt-8 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">Regional Agriculture Company</h3>
                  <p className="text-sm text-gray-700">How We Helped Use AI to Optimize Crop Yields</p>
                  <div className="mt-4 space-y-2">
                    <p className="text-sm font-semibold">Before:</p>
                    <p className="text-sm text-gray-700">Inconsistent crop yields due to unpredictable weather patterns</p>
                    <p className="text-sm font-semibold">After:</p>
                    <p className="text-sm text-gray-700">
                      20% increase in crop yield using AI-powered weather prediction and irrigation optimization
                    </p>
                  </div>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">Local Healthcare Provider</h3>
                  <p className="text-sm text-gray-700">Implementing Blockchain for Secure Patient Records</p>
                  <div className="mt-4 space-y-2">
                    <p className="text-sm font-semibold">Before:</p>
                    <p className="text-sm text-gray-700">Fragmented patient data across multiple systems</p>
                    <p className="text-sm font-semibold">After:</p>
                    <p className="text-sm text-gray-700">
                      Unified, secure patient records with 99.9% uptime and HIPAA compliance
                    </p>
                  </div>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">Boutique Manufacturing Firm</h3>
                  <p className="text-sm text-gray-700">Custom Software for Inventory Management</p>
                  <div className="mt-4 space-y-2">
                    <p className="text-sm font-semibold">Before:</p>
                    <p className="text-sm text-gray-700">Manual inventory tracking leading to frequent stockouts</p>
                    <p className="text-sm font-semibold">After:</p>
                    <p className="text-sm text-gray-700">
                      Automated inventory system reduced stockouts by 95% and improved cash flow
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">What We Offer</h2>
            <div className="mt-8 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">AI Consultation and Roadmap Development</h3>
                  <p className="mt-2 text-gray-700">For companies just exploring the tech</p>
                  <ul className="mt-4 space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">AI readiness assessment</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Custom AI strategy development</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Implementation roadmap</span>
                    </li>
                  </ul>
                  <Button className="mt-6 w-full" variant="outline">
                    Learn More
                  </Button>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">End-to-End Solution Development</h3>
                  <p className="mt-2 text-gray-700">For organizations ready to implement</p>
                  <ul className="mt-4 space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Custom AI model development</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Blockchain integration</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Full-stack software development</span>
                    </li>
                  </ul>
                  <Button className="mt-6 w-full" variant="outline">
                    Schedule a Consultation
                  </Button>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-2xl font-bold">Tech Stack Optimization and Maintenance</h3>
                  <p className="mt-2 text-gray-700">For businesses needing ongoing support</p>
                  <ul className="mt-4 space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Performance optimization</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Security audits and updates</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="mr-2 h-4 w-4 text-green-500" />
                      <span className="text-sm">Continuous improvement and scaling</span>
                    </li>
                  </ul>
                  <Button className="mt-6 w-full" variant="outline">
                    Get Support
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              Why Businesses Trust Us with Their Tech Transformation
            </h2>
            <div className="mt-8 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-xl font-bold">John Doe, CEO of AgriTech Solutions</h3>
                  <p className="mt-2 text-gray-700">
                    "Their AI solutions have revolutionized our crop management. We've seen a 30% increase in efficiency."
                  </p>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-xl font-bold">Jane Smith, CTO of HealthCare Plus</h3>
                  <p className="mt-2 text-gray-700">
                    "The blockchain solution they implemented has made our patient data management seamless and secure."
                  </p>
                </div>
              </div>
              <div className="rounded-lg border bg-card text-card-foreground shadow-sm">
                <div className="p-6">
                  <h3 className="text-xl font-bold">Mike Johnson, Owner of Craft Manufacturing Co.</h3>
                  <p className="mt-2 text-gray-700">
                    "Their custom software has streamlined our operations, saving us time and money."
                  </p>
                </div>
              </div>
            </div>
            <div className="mt-12 flex flex-wrap items-center justify-center gap-6">
              <div className="flex items-center space-x-2">
                <CheckCircle className="h-5 w-5 text-green-500" />
                <span className="text-sm font-medium">ISO 27001 Certified</span>
              </div>
              <div className="flex items-center space-x-2">
                <CheckCircle className="h-5 w-5 text-green-500" />
                <span className="text-sm font-medium">Google Cloud Partner</span>
              </div>
              <div className="flex items-center space-x-2">
                <CheckCircle className="h-5 w-5 text-green-500" />
                <span className="text-sm font-medium">Microsoft Gold Partner</span>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Our Expertise in the Latest Tech</h2>
            <div className="mt-8 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
              <div className="flex items-center space-x-4">
                <Code className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">TensorFlow</h3>
                  <p className="text-sm text-gray-700">Advanced machine learning and neural networks</p>
                </div>
              </div>
              <div className="flex items-center space-x-4">
                <Database className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">Ethereum</h3>
                  <p className="text-sm text-gray-700">Smart contracts and decentralized applications</p>
                </div>
              </div>
              <div className="flex items-center space-x-4">
                <Code className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">Python</h3>
                  <p className="text-sm text-gray-700">Versatile programming for AI and data science</p>
                </div>
              </div>
              <div className="flex items-center space-x-4">
                <Database className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">AWS</h3>
                  <p className="text-sm text-gray-700">Cloud computing and serverless architecture</p>
                </div>
              </div>
              <div className="flex items-center space-x-4">
                <Code className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">React</h3>
                  <p className="text-sm text-gray-700">Modern, responsive web applications</p>
                </div>
              </div>
              <div className="flex items-center space-x-4">
                <Database className="h-8 w-8" />
                <div>
                  <h3 className="font-bold">PostgreSQL</h3>
                  <p className="text-sm text-gray-700">Robust, scalable database solutions</p>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-black text-white">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
                  Ready to Explore Custom AI Solutions for Your Niche?
                </h2>
                <p className="mx-auto max-w-[700px] text-gray-300 md:text-xl">
                  Let's discuss how we can transform your business with tailored technology solutions.
                </p>
              </div>
              <div className="w-full max-w-sm space-y-2">
                <form className="flex space-x-2">
                  <Input
                    className="max-w-lg flex-1 bg-gray-800 text-white border-gray-700"
                    placeholder="Enter your email"
                    type="email"
                  />
                  <Button type="submit">Book Your Free Consultation Now</Button>
                </form>
              </div>
            </div>
          </div>
        </section>
        <section id="faq" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Frequently Asked Questions</h2>
            <div className="mt-8">
              <Accordion type="single" collapsible className="w-full">
                <AccordionItem value="item-1">
                  <AccordionTrigger>How long does a typical project take?</AccordionTrigger>
                  <AccordionContent>
                    Project timelines vary depending on complexity and scope. A small AI implementation might take 2-3 months,
                    while a full-scale blockchain solution could take 6-12 months. We'll provide a detailed timeline during our
                    initial consultation.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-2">
                  <AccordionTrigger>What industries do you specialize in?</AccordionTrigger>
                  <AccordionContent>
                    We have experience across various industries including healthcare, agriculture, manufacturing, finance,
                    and logistics. Our team adapts quickly to new domains, allowing us to serve niche markets effectively.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-3">
                  <AccordionTrigger>What if I don't know what solution I need yet?</AccordionTrigger>
                  <AccordionContent>
                    That's perfectly fine! Our consultation process is designed to help you identify the best technological
                    approach for your business challenges. We'll work with you to understand your needs and recommend
                    appropriate solutions.
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </div>
          </div>
        </section>
      </main>
      <footer id="contact" className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-gray-700">© 2024 AI Consulting. All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
        </nav>
        <Button className="ml-4" variant="outline">
          Schedule a Free Consultation
        </Button>
      </footer>
    </div>
  )
}