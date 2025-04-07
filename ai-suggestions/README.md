AI tools are excellent for making suggestions and assisting with rapidly developing code.
It is a tool that is most useful when the user can understand 

1) proper question syntax
2) the validity of the response given by the AI agent
3) the intent of the user


I used AI agents to generate a Powershell equivalent (DNS_Dig_script_in_PowerShell.ps1)
of the originally produced python script as preferred in the original request, but
I don't have enough personal knowledge of Powershell syntax to comfortably recommend
it at this point. However, it does execute and produces the output as seen in the
AI-recommendations directory. Note the additional whitespace newline.

I do not plan on further refining this example at this time.

Additionally, I requested recommendations for improving the original python
script (AI-recommendations.txt). I can agree with all of the practices returned by
the AI, but would stress that, in the context of such a simple script, features such
as error logging to an external file would be unnecessary, and a need to include
command validation for a basic system utility like 'dig' with more user friendly
logging would  suggest that the user is dangerously unaware of the system.

It is important to note that AI will always make suggestions when asked unless
otherwise programmed not to (such as in the case of not refining malware). I repeated 
this particular process recursively just to see the output, and the code produced 
was more and more functional, but less and less readable.

AI's most powerful function in writing code is to help the developer understand
options and alternatives, making us better programmers, but critical thinking is
still required to produced a quality product.
