Ip: ${answers[0]['addr']} - Country: ${answers[0]['country_code']}

%for a in answers:
${a['host']} \
%for k in a['keywords']:
- ${k} \
%endfor

%endfor
