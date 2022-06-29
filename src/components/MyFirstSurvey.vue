<template>
  <Survey :survey="survey" />
</template>

<script>
// Modern theme
import 'survey-core/modern.min.css';
// Default V2 theme
// import 'survey-core/defaultV2.min.css';
import { Model, StylesManager } from 'survey-core';
import { Survey } from 'survey-vue-ui';

// const SURVEY_ID = 1;

StylesManager.applyTheme("modern");

const surveyJson = 
{
 title: "NFTTTTT",
 logoPosition: "right",
 completedHtml: "<h3>Thank you for your feedback.</h3> <h5>Your thoughts and ideas will help us to create a great product!</h5><div style=\"margin: 32px 0;\"><button class=\"rounded-button rounded-button--small\" onclick=\"reRunSurvey();\">Run survey again</button></div>",
 completedHtmlOnCondition: [
  {
   html: "<h3>Thank you for your feedback.</h3> <h5>We glad that you love our product. Your ideas and suggestions will help us to make our product even better!</h5>"
  },
  {
   html: "<h3>Thank you for your feedback.</h3> <h5> We are glad that you share with us your ideas.We highly value all suggestions from our customers. We do our best to improve the product and reach your expectation.</h5><br/>"
  }
 ],
 pages: [
  {
   name: "page1",
   elements: [
    {
     type: "imagepicker",
     name: "Original_Face",
     title: "捏脸",
     choices: [
      {
       value: "lion",
       imageLink: "https://surveyjs.io/Content/Images/examples/image-picker/lion.jpg"
      },
      {
       value: "giraffe",
       imageLink: "https://surveyjs.io/Content/Images/examples/image-picker/giraffe.jpg"
      },
      {
       value: "panda",
       imageLink: "https://surveyjs.io/Content/Images/examples/image-picker/panda.jpg"
      },
      {
       value: "camel",
       imageLink: "https://surveyjs.io/Content/Images/examples/image-picker/camel.jpg"
      }
     ]
    },
    {
     type: "checkbox",
     name: "Major",
     title: "选择专业",
     choices: [
      {
       value: "item1",
       text: "人文学部"
      },
      {
       value: "item2",
       text: "社会学部"
      },
      {
       value: "item3",
       text: "经济学部"
      },
      {
       value: "item4",
       text: "法政学部"
      },
      {
       value: "item5",
       text: "理工学部"
      }
     ]
    },
    {
     type: "ranking",
     name: "Weekend",
     title: "偏爱如何度过周末（排序）",
     choices: [
      {
       value: "item1",
       text: "在图书馆畅游梦乡...不是，畅游学海"
      },
      {
       value: "item2",
       text: "去食堂尽情品尝后厨阿姨的创意新品"
      },
      {
       value: "item5",
       text: "世纪馆的健身房，如果你是那个预约成功的幸运儿..."
      },
      {
       value: "item3",
       text: "去超市进行新一周的物资采购吧"
      },
      {
       value: "item4",
       text: "超喜欢在明德楼的，这里老师讲课好听，人才又多"
      },
      {
       value: "item7",
       text: "和朋友们一起去球场！"
      },
      {
       value: "item6",
       text: "还是待在宿舍吧"
      }
     ]
    }
   ]
  }
 ],
 showQuestionNumbers: "off"
}

export default {
  name: 'MyFirstSurvey',
  components: {
    Survey
  },
  data() {
    const survey = new Model(surveyJson);
    survey.onComplete.add(this.alertResults);

    return {
      survey
    }
  },
  methods: {
    alertResults (sender) {
      const results = JSON.stringify(sender.data);
      document.write(results);
      // saveSurveyResults(
      //   "https://your-web-service.com/" + SURVEY_ID,
      //   sender.data
      // )
    }
    
  },
}

// function saveSurveyResults(url, json) {
//   const request = new XMLHttpRequest();
//   request.open('POST', url);
//   request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
//   request.addEventListener('load', () => {
//     // Handle "load"
//   });
//   request.addEventListener('error', () => {
//     // Handle "error"
//   });
//   request.send(JSON.stringify(json));
// }
</script>
