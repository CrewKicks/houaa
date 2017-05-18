from subprocess import call

call(['npm','run','build'])
call(['cp','dist/static/sw.js','dist/'])
call(['cp','dist/static/serviceworker-cache-polyfill.js','dist/'])
# call(['rsync','-avzhe','ssh','dist/index.html','root@101.200.46.157:/usr/share/nginx/frontend'])
# call(['rsync','-avzhe','ssh','dist/static','root@101.200.46.157:/usr/share/nginx/frontend'])
