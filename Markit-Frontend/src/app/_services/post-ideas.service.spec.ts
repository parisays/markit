import { TestBed } from '@angular/core/testing';

import { PostIdeasService } from './post-ideas.service';

describe('PostIdeasService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PostIdeasService = TestBed.get(PostIdeasService);
    expect(service).toBeTruthy();
  });
});
