import {async, getTestBed, TestBed} from '@angular/core/testing';
import {HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import {PostIdeasService} from './post-ideas.service';
import {DataService} from '@app/_services/data.service';
import {environment} from '@environments/environment';

fdescribe('PostIdeasService', () => {
  // let injector: TestBed;
  // let httpMock: HttpTestingController;
  let postIdeaService: PostIdeasService;
  let dataService: DataService;
  let dataServiceSpy: jasmine.SpyObj<DataService>;

  beforeEach(async(() => {
    const spy = jasmine.createSpyObj('DataService', ['getAll']);
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [
        PostIdeasService,
        {provide: DataService, useValue: spy}
      ]
    });
    postIdeaService = TestBed.get(PostIdeasService);
    dataServiceSpy = TestBed.get(DataService);
    // dataService = TestBed.get(DataService);

    // injector = getTestBed();
    // service = injector.get(PostIdeasService);
    // httpMock = injector.get(HttpTestingController);
  }));

  //
  // afterEach(() => {
  //   httpMock.verify();
  // });

  it('should be created', () => {
    // const service: PostIdeasService = TestBed.get(PostIdeasService);
    expect(postIdeaService).toBeTruthy();
  });

  it('getall post ideas should return real data form real service', () => {
    expect(dataService.getAll(null, `${environment.apiUrl}socials/twitter/trends/`)).toBe('real data');
  });

  // const dummyPostIdeasResponse = {
  //   data:
  //     [
  //       {type: 'twitter', label: '#BeBest', text: 'http://twitter.com/search?q=%23BeBest'},
  //       {type: 'twitter', label: 'Greta', text: 'http://twitter.com/search?q=Greta'},
  //       {type: 'twitter', label: 'Yankees', text: 'http://twitter.com/search?q='},
  //       {type: 'twitter', label: 'RHONJ', text: 'http://twitter.com/search?q=%23RHONJ'},
  //     ]
  // };

  // it('getall post ideas', () => {
  //   service.getAll().subscribe(response => {
  //     expect(response).toEqual(dummyPostIdeasResponse);
  //   });
  //
  //   const req = httpMock.expectOne(`${environment.apiUrl}
  socials / twitter / trends / `);
  //   expect(req.request.method).toBe('GET');
  //   req.flush(dummyPostIdeasResponse);
  // });
});
