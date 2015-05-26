def domain_name(url):
    step = url.rsplit('.', 1)[0]
    step2 = step[7:]

    if "www." in step2:
        step2 = step2[4:]

    return step2

domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
