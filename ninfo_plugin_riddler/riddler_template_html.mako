Ip: ${answers[0]['addr']} - Country: ${answers[0]['country_code']}
%for a in answers:
    <br><b>${a['host']}</b><br>
%for k in a['keywords']:
        &nbsp;<i>${k}</i>
%endfor

%endfor
