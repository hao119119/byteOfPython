<!DOCTYP html>
<html>
<head>
    <title>hello world</title>
    <body>
        <p>
            welcome {{username}}
        </p>
        <ul>
            %for thing in things:
                <li>{{thing}}</li>
            %end
        </ul>
        <form action="/favorite_fruit" method="POST">
            what is your favorite fruit?
            <input type="text" name="fruit" size="40" value=""><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</head>
</html>