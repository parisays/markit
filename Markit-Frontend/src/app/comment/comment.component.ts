import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {

  submitting = false;
  user = {
    author: 'Han Solo',
    avatar: '../../assets/images/user-logo.png'
  };
  inputValue = '';

  data = [
    {
      author: 'Han Solo',
      avatar: '../../assets/images/user-logo.png',
      content:
        'We supply a series of design principles, practical patterns and high quality design resources' +
        '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    //   children: [
    //     {
    //       author: 'Han Solo',
    //       avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //       content:
    //         'We supply a series of design principles, practical patterns and high quality design resources' +
    //         '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    //       children: [
    //         {
    //           author: 'Han Solo',
    //           avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //           content:
    //             'We supply a series of design principles, practical patterns and high quality design resources' +
    //             '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    //             children: [
    //               {
    //                 author: 'Han Solo',
    //                 avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //                 content:
    //                   'We supply a series of design principles, practical patterns and high quality design resources' +
    //                   '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    //               },
    //               {
    //                 author: 'Han Solo',
    //                 avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //                 content:
    //                   'We supply a series of design principles, practical patterns and high quality design resources' +
    //                   '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    //               }
    //             ]
    //         },
    //         {
    //           author: 'Han Solo',
    //           avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //           content:
    //             'We supply a series of design principles, practical patterns and high quality design resources' +
    //             '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    //         }
    //       ]
    //     }
    //   ]
    },
    {
      author: 'Han Solo',
      avatar: '../../assets/images/user-logo.png',
      content:
        'We supply a series of design principles, practical patterns and high quality design resources' +
        '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
