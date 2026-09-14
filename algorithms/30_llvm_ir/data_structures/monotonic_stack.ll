; ModuleID = 'algorithms/02_c/data_structures/monotonic_stack.c'
source_filename = "algorithms/02_c/data_structures/monotonic_stack.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [56 x i8] c"[C MonotonicStack] FAILED at index %d: got %d, want %d\0A\00", align 1
@str = private unnamed_addr constant [49 x i8] c"[C MonotonicStack] Next greater element verified\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @next_greater(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef writeonly captures(none) %2) local_unnamed_addr #0 {
  %4 = alloca [100000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #5
  %5 = icmp sgt i32 %1, 0
  br i1 %5, label %6, label %16

6:                                                ; preds = %3
  %7 = zext nneg i32 %1 to i64
  br label %8

8:                                                ; preds = %6, %26
  %9 = phi i64 [ %7, %6 ], [ %11, %26 ]
  %10 = phi i32 [ -1, %6 ], [ %32, %26 ]
  %11 = add nsw i64 %9, -1
  %12 = icmp sgt i32 %10, -1
  br i1 %12, label %13, label %26

13:                                               ; preds = %8
  %14 = getelementptr inbounds i32, ptr %0, i64 %11
  %15 = load i32, ptr %14, align 4, !tbaa !5
  br label %17

16:                                               ; preds = %26, %3
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #5
  ret void

17:                                               ; preds = %13, %23
  %18 = phi i32 [ %10, %13 ], [ %24, %23 ]
  %19 = zext nneg i32 %18 to i64
  %20 = getelementptr inbounds nuw i32, ptr %4, i64 %19
  %21 = load i32, ptr %20, align 4, !tbaa !5
  %22 = icmp sgt i32 %21, %15
  br i1 %22, label %26, label %23

23:                                               ; preds = %17
  %24 = add nsw i32 %18, -1
  %25 = icmp sgt i32 %18, 0
  br i1 %25, label %17, label %26, !llvm.loop !9

26:                                               ; preds = %23, %17, %8
  %27 = phi i32 [ %10, %8 ], [ %18, %17 ], [ -1, %23 ]
  %28 = phi i32 [ -1, %8 ], [ %21, %17 ], [ -1, %23 ]
  %29 = getelementptr inbounds i32, ptr %2, i64 %11
  store i32 %28, ptr %29, align 4, !tbaa !5
  %30 = getelementptr inbounds i32, ptr %0, i64 %11
  %31 = load i32, ptr %30, align 4, !tbaa !5
  %32 = add nsw i32 %27, 1
  %33 = sext i32 %32 to i64
  %34 = getelementptr inbounds i32, ptr %4, i64 %33
  store i32 %31, ptr %34, align 4, !tbaa !5
  %35 = icmp sgt i64 %9, 1
  br i1 %35, label %8, label %16, !llvm.loop !11
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [100000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  store i32 10, ptr %1, align 16, !tbaa !5
  %2 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 2, ptr %2, align 4, !tbaa !5
  %3 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %4 = load i32, ptr %3, align 4, !tbaa !5
  %5 = icmp sgt i32 %4, 5
  br i1 %5, label %10, label %6

6:                                                ; preds = %0
  %7 = load i32, ptr %1, align 16, !tbaa !5
  %8 = icmp sgt i32 %7, 5
  br i1 %8, label %10, label %9

9:                                                ; preds = %6
  br label %10

10:                                               ; preds = %9, %6, %0
  %11 = phi i1 [ true, %0 ], [ false, %9 ], [ true, %6 ]
  %12 = phi i32 [ 1, %0 ], [ -1, %9 ], [ 0, %6 ]
  %13 = phi i32 [ %4, %0 ], [ -1, %9 ], [ %7, %6 ]
  %14 = add nsw i32 %12, 1
  %15 = zext nneg i32 %14 to i64
  %16 = getelementptr inbounds nuw i32, ptr %1, i64 %15
  store i32 5, ptr %16, align 4, !tbaa !5
  %17 = zext nneg i32 %14 to i64
  %18 = getelementptr inbounds nuw i32, ptr %1, i64 %17
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = icmp sgt i32 %19, 4
  br i1 %20, label %35, label %21

21:                                               ; preds = %10
  br i1 %11, label %22, label %34, !llvm.loop !9

22:                                               ; preds = %21
  %23 = zext nneg i32 %12 to i64
  %24 = getelementptr inbounds nuw i32, ptr %1, i64 %23
  %25 = load i32, ptr %24, align 4, !tbaa !5
  %26 = icmp sgt i32 %25, 4
  br i1 %26, label %35, label %27

27:                                               ; preds = %22
  br i1 %5, label %28, label %34, !llvm.loop !9

28:                                               ; preds = %27
  %29 = sext i32 %12 to i64
  %30 = getelementptr i32, ptr %1, i64 %29
  %31 = getelementptr i8, ptr %30, i64 -4
  %32 = load i32, ptr %31, align 4, !tbaa !5
  %33 = icmp sgt i32 %32, 4
  br i1 %33, label %35, label %34

34:                                               ; preds = %28, %27, %21
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  br label %42

35:                                               ; preds = %28, %22, %10
  %36 = phi i32 [ %19, %10 ], [ %25, %22 ], [ %32, %28 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  %37 = icmp eq i32 %36, 5
  br i1 %37, label %38, label %42

38:                                               ; preds = %35
  %39 = icmp eq i32 %13, 10
  br i1 %39, label %40, label %42

40:                                               ; preds = %38
  %41 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %47

42:                                               ; preds = %34, %38, %35
  %43 = phi i32 [ 0, %35 ], [ 1, %38 ], [ 0, %34 ]
  %44 = phi i32 [ %36, %35 ], [ %13, %38 ], [ -1, %34 ]
  %45 = phi i32 [ 5, %35 ], [ 10, %38 ], [ 5, %34 ]
  %46 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %43, i32 noundef %44, i32 noundef %45)
  br label %47

47:                                               ; preds = %42, %40
  %48 = phi i32 [ 0, %40 ], [ 1, %42 ]
  ret i32 %48
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind }
attributes #5 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
