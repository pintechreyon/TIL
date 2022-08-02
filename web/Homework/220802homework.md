1. Semantic Tag 

   보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱(semantic) 태그를 모두 고르시오.

   ```bash
   div, header*, h1, section*, footer*, a, form, span
   ```

   

2. input Tag 

   아래 이미지와 같이 로그인 Form을 생성하는 HTML코드를 작성하시오.  단, USERNAME 글자를 클릭하면 아이디를 입력하는 input에, PWD 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 되도록 하시오.

​                       [![123.png](https://i.postimg.cc/zDWM8Pmj/123.png)](https://postimg.cc/qgJQGwvh)

​	

```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>로그인 폼</title>
  </head>
  <body>
      <h3>로그인 폼</h3>
      <hr>
      <form name="fo" method="get">
        <b>USERNAME : <input type="text" size="15" placeholder="아이디를 입력하세요" value=""></b><br>
        <b>PWD : <input type="password" size="15" value=""></b>
        <input type="submit" value="완료">
      </form>
  </body>
</html>
```





3. 크기 단위 크기 

   단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

   ```bash
   rem
   ```

   

4. 선택자 

   다음 예제를 통해 ‘자손 결합자’와 ‘자식 결합자’의 차이를 설명하시오.



​                       [![411.png](https://i.postimg.cc/hthNW4KJ/411.png)](https://postimg.cc/WdL50vFj)

```bash
span태그로 감싸져있는 부분에 대해 자손 결합자는 관여되고 자식결합자는 관여하지 않는다
```

